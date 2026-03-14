import os
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SRC = r'C:\ai-projects\skip-school\site\files\src'

# FAQ data: slug -> list of (question, answer) tuples
faqs = {
    '05-ai-curriculum-builder': [
        ("What AI tools can I use to build a homeschool curriculum?", "ChatGPT and Claude are the two most popular AI tools for building homeschool curricula. Both can generate lesson plans, suggest resources, and create custom scope-and-sequence documents tailored to your child's grade level and learning style."),
        ("How long does it take to build an AI curriculum?", "Most parents can create a full weekly curriculum in about 45 minutes once they learn the right prompts. The first time takes longer as you refine your approach, but after a few weeks it becomes a quick Sunday evening routine."),
        ("Is an AI-generated curriculum as good as a boxed curriculum?", "An AI curriculum can be more personalized than a boxed curriculum because it adapts to your child's specific interests, pace, and learning style. However, it requires more parent involvement in reviewing and curating the output."),
    ],
    '06-chatgpt-vs-claude-homeschool': [
        ("Which is better for homeschooling, ChatGPT or Claude?", "Both are excellent. ChatGPT tends to be more creative and widely known, while Claude often produces more structured, detailed lesson plans. Many homeschool parents use both for different tasks."),
        ("Is ChatGPT free to use for homeschooling?", "ChatGPT offers a free tier with limited access to GPT-3.5. For more advanced features and GPT-4 access, you need ChatGPT Plus at $20/month. Claude also offers a free tier with daily limits."),
        ("Can kids use ChatGPT or Claude safely?", "Both tools have content safety measures, but parental supervision is recommended for younger children. Setting up the AI with specific instructions about age-appropriate content adds an extra layer of safety."),
    ],
    '07-socialization-myth': [
        ("How do homeschooled kids socialize?", "Homeschooled kids socialize through co-ops, sports teams, community classes, church groups, neighborhood play, and volunteer work. Many homeschool families report their children develop stronger social skills because they interact with diverse age groups."),
        ("Are homeschooled kids less social than public school kids?", "Research consistently shows homeschooled students are not at a social disadvantage. Studies from the National Home Education Research Institute show homeschooled children score above average on measures of social development and emotional health."),
        ("How many hours per day do homeschooled kids need with other kids?", "There is no set requirement. Quality matters more than quantity. Regular weekly activities with peers, combined with family interactions and community involvement, provide ample socialization for most children."),
    ],
    '08-morning-routine-ai': [
        ("What does an AI homeschool morning routine look like?", "A typical AI-powered morning starts with 30 minutes of independent reading, followed by an AI-generated math lesson, then a writing or language arts session. The AI helps plan the specific activities and adjust difficulty based on progress."),
        ("How many hours should a homeschool day be?", "Most homeschool families find 3-4 hours of focused instruction is sufficient for elementary students and 4-5 hours for high schoolers. AI tools help maximize efficiency so learning time is more productive."),
        ("Should I follow a strict schedule for homeschool?", "A flexible routine works better than a rigid schedule for most families. Having consistent blocks for core subjects while allowing flexibility for interest-led learning helps maintain structure without creating stress."),
    ],
    '09-first-week-ai-homeschool': [
        ("What should I do the first week of homeschooling with AI?", "Start by exploring one AI tool (like ChatGPT or Claude) with simple tasks: generate a reading list, create a math worksheet, or plan one lesson. Do not try to overhaul your entire curriculum in week one."),
        ("How do I start homeschooling with no experience?", "Begin by checking your state's homeschool laws, then choose 2-3 core subjects to focus on initially. Use AI to help plan lessons and find resources. Many families find their rhythm within the first month."),
        ("What supplies do I need to start AI homeschooling?", "You need a computer or tablet with internet access, basic school supplies (notebooks, pencils), and access to an AI tool like ChatGPT or Claude. A printer is helpful but not essential."),
    ],
    '10-khan-academy-guide': [
        ("Is Khan Academy good for homeschooling?", "Khan Academy is one of the best free resources for homeschooling, especially for math and science. It offers structured courses, practice exercises, and progress tracking that make it easy to use as a core curriculum component."),
        ("How do I set up Khan Academy for my homeschool?", "Create a parent account, then add your children as students. Assign specific courses or let them explore. The Khanmigo AI tutor provides personalized help and can guide students through difficult concepts."),
        ("Is Khan Academy enough for a complete homeschool curriculum?", "Khan Academy covers math, science, computing, and some humanities comprehensively, but you will want to supplement with additional resources for language arts, writing, and hands-on projects."),
    ],
    '11-homeschool-on-budget': [
        ("Can you homeschool for free?", "Yes, it is possible to homeschool for $0 using free resources like Khan Academy, library materials, YouTube educational channels, and AI tools with free tiers. Many excellent curriculum options are completely free."),
        ("How much does homeschooling cost per year?", "Homeschooling costs range from $0 to $2,000+ per year depending on your approach. Using AI tools and free online resources can keep costs minimal, while boxed curricula and online classes add to the expense."),
        ("What are the best free homeschool resources?", "Top free resources include Khan Academy, ChatGPT/Claude free tiers, your local library, PBS LearningMedia, CK-12, and YouTube channels like CrashCourse and SciShow Kids."),
    ],
    '12-ai-reading-list-by-age': [
        ("How do I choose the right books for my child's reading level?", "AI tools can assess your child's current reading level based on books they have enjoyed and suggest titles at an appropriate challenge level. Look for books that are slightly above their comfort zone to encourage growth."),
        ("How many books should a homeschooled child read per year?", "There is no magic number, but most educators suggest 25-40 books per year for elementary students. Focus on variety across genres and gradually increasing complexity rather than hitting a specific count."),
        ("Can AI recommend books for reluctant readers?", "Yes. AI can suggest high-interest, lower-reading-level books that match your child's specific interests. Graphic novels, choose-your-own-adventure books, and series with cliffhanger endings often engage reluctant readers."),
    ],
    '13-teach-kids-use-ai': [
        ("At what age can kids start using AI tools?", "Children as young as 8-9 can begin using AI with direct parental supervision. By ages 11-12, many kids can use AI more independently with clear guidelines. The key is teaching them to evaluate AI output critically."),
        ("Is AI safe for children to use?", "AI tools like ChatGPT and Claude have content safety filters, but they are not foolproof. Parental supervision, setting clear usage rules, and teaching kids to think critically about AI responses are essential safety measures."),
        ("How do I teach my child not to rely on AI for answers?", "Frame AI as a thinking partner, not an answer machine. Teach kids to ask AI questions that help them learn, not just get answers. Have them explain AI responses in their own words and fact-check key claims."),
    ],
    '14-homeschool-field-trip-ideas': [
        ("How often should homeschoolers go on field trips?", "Most homeschool families do 1-2 field trips per month. These can range from local library visits and nature walks to museum trips and factory tours. Consistency matters more than frequency."),
        ("Do homeschool field trips count as school?", "Yes, field trips absolutely count as educational time. Many states recognize experiential learning as part of your homeschool curriculum. Document field trips in your records for portfolio reviews if required."),
        ("What are the best free field trip ideas?", "Parks, nature preserves, libraries, local government buildings, fire stations, community gardens, and free museum days all make excellent no-cost field trips that provide real-world learning opportunities."),
    ],
    '15-charlotte-mason-ai': [
        ("What is the Charlotte Mason method of homeschooling?", "Charlotte Mason is an educational philosophy emphasizing living books (not textbooks), nature study, short lessons, narration, and the development of good habits. It treats children as whole persons deserving a rich, broad curriculum."),
        ("How does AI fit with Charlotte Mason homeschooling?", "AI can enhance Charlotte Mason education by curating living book lists, generating nature study guides, creating narration prompts, and helping plan picture study and composer study rotations while preserving the method's emphasis on real books and nature."),
        ("Can you do Charlotte Mason homeschool on a budget?", "Charlotte Mason is naturally budget-friendly because it relies heavily on library books, outdoor time, and simple art supplies. AI tools make it even more affordable by replacing expensive curriculum guides with free, personalized planning."),
    ],
    '16-classical-education-ai': [
        ("What is classical education homeschooling?", "Classical education follows the Trivium: Grammar (K-5, memorization and facts), Logic (6-8, analysis and reasoning), and Rhetoric (9-12, persuasive communication). It emphasizes great books, Latin, logic, and the liberal arts."),
        ("How can AI help with classical homeschooling?", "AI can generate Latin vocabulary drills, create Socratic discussion questions, suggest great books by period, build timeline activities, and help plan rhetoric exercises. It is particularly useful for the Logic stage where analytical thinking is developed."),
        ("Is classical education better than other homeschool methods?", "No method is universally better. Classical education excels at developing critical thinking and communication skills. It works well for families who value rigorous academics and the Western intellectual tradition."),
    ],
    '17-homeschool-writing-ai': [
        ("How do I teach writing without AI doing it for my child?", "Use AI as a brainstorming partner and editor, not a ghostwriter. Have your child draft first, then use AI to suggest improvements. Teach them to use AI for outlining ideas and getting feedback on their own writing."),
        ("At what age should kids start writing with AI assistance?", "Children can begin using AI for writing support around age 9-10, starting with brainstorming prompts and vocabulary suggestions. By middle school, they can use AI for more advanced editing and feedback on structure."),
        ("What are good AI writing prompts for kids?", "Start with creative prompts like 'Write a story where you are an explorer who discovers...' or informational prompts like 'Explain how volcanoes work to a friend.' AI can generate age-appropriate prompts tailored to your child's interests."),
    ],
    '18-ai-science-experiments': [
        ("Can AI design safe science experiments for kids?", "Yes. AI can generate age-appropriate experiments using common household materials. Always review the experiment details before starting and supervise children during any hands-on activity."),
        ("What supplies do I need for AI-generated science experiments?", "Most AI-designed experiments use common kitchen items: baking soda, vinegar, food coloring, water, cups, and basic measuring tools. The AI specifically designs experiments around materials you already have."),
        ("How do I make science hands-on without a lab?", "Your kitchen is a lab. AI can design experiments using everyday materials that teach the same principles as traditional lab work. Nature walks, gardening, and cooking also provide excellent hands-on science opportunities."),
    ],
    '19-high-school-ai': [
        ("Can you homeschool high school with AI?", "Absolutely. AI tools can help create rigorous high school courses, generate practice problems for standardized tests, provide writing feedback at the college prep level, and help plan a transcript-worthy curriculum."),
        ("Do colleges accept homeschooled students?", "Yes. All major colleges and universities accept homeschool applicants. Many have specific admissions processes for homeschoolers. Strong standardized test scores, detailed transcripts, and extracurriculars strengthen applications."),
        ("How do I create a homeschool high school transcript?", "List each course with the year completed, credit hours, and grade. Include a course description document. AI can help format transcripts to match college expectations and ensure you have covered standard requirements."),
    ],
    '20-special-needs-ai': [
        ("Can AI help with special needs homeschooling?", "AI excels at adapting content to individual learning needs. It can simplify text, create visual aids, generate repetitive practice in varied formats, and adjust pacing. Many parents of children with learning differences find AI invaluable."),
        ("What AI tools are best for dyslexic learners?", "AI text-to-speech tools, audiobook generators, and tools that create content with dyslexia-friendly formatting are particularly helpful. ChatGPT and Claude can also simplify complex text and generate multi-sensory learning activities."),
        ("Is homeschooling better for kids with ADHD?", "Many families find homeschooling beneficial for kids with ADHD because it allows flexible scheduling, movement breaks, interest-led learning, and the ability to work during the child's peak focus times."),
    ],
    '21-ai-math-help': [
        ("How can AI help my child with math?", "AI can generate practice problems at your child's level, explain concepts in multiple ways, create visual representations, and provide step-by-step solutions. It acts as a patient, always-available math tutor."),
        ("Is AI good at teaching math to kids?", "AI is excellent at math instruction because it can adapt explanations to your child's level, generate unlimited practice problems, and never loses patience. It works best alongside hands-on manipulatives for younger children."),
        ("What if AI gives wrong math answers?", "AI occasionally makes calculation errors, especially with complex arithmetic. Always verify important answers and teach your child to double-check AI math work. This is actually a good critical thinking exercise."),
    ],
    '22-screen-time-balance': [
        ("How much screen time is OK for homeschool?", "Most experts suggest keeping educational screen time to 2-3 hours for elementary students and 3-4 hours for older students. Mix screen-based AI activities with offline projects, outdoor time, and hands-on learning."),
        ("Does AI homeschooling mean more screen time?", "Not necessarily. You can use AI for planning and resource generation offline, then implement those plans without screens. Many AI-generated activities like science experiments, art projects, and nature journals are screen-free."),
        ("How do I balance AI learning with outdoor time?", "Schedule AI-assisted learning for mornings and reserve afternoons for outdoor activities, sports, and hands-on projects. Use AI to design outdoor scavenger hunts, nature studies, and field trip activities."),
    ],
    '23-state-homeschool-laws': [
        ("Do I need permission to homeschool my child?", "Requirements vary by state. Some states require notification only, while others require standardized testing or portfolio reviews. Check your specific state's laws before starting."),
        ("Which states are easiest to homeschool in?", "States with the most homeschool freedom include Texas, Alaska, Idaho, and Iowa, which have minimal reporting requirements. States like New York and Pennsylvania have more regulations."),
        ("Do homeschooled kids need to take state tests?", "Testing requirements vary by state. Some states require annual standardized testing, others require periodic assessments, and many states have no testing requirements at all for homeschoolers."),
    ],
    '24-homeschool-co-op-guide': [
        ("What is a homeschool co-op?", "A homeschool co-op is a group of families who meet regularly to share teaching responsibilities, provide group classes, and create social opportunities for their children. They range from informal playgroups to structured learning communities."),
        ("How do I find homeschool co-ops near me?", "Search Facebook groups for '[your city] homeschool co-op,' check local library bulletin boards, ask at churches, and search directories on HSLDA.org or your state's homeschool association website."),
        ("How much do homeschool co-ops cost?", "Most co-ops charge $50-200 per semester to cover supplies and facility rental. Some are completely free and run by parent volunteers. University-model co-ops or enrichment programs can cost $1,000-3,000+ per year."),
    ],
    '25-ai-for-reluctant-learner': [
        ("How do I motivate a child who hates school?", "Start with their interests. If they love dinosaurs, build lessons around paleontology. AI can generate engaging, interest-based content that makes learning feel less like school. Short sessions and frequent breaks also help."),
        ("Can AI make learning fun for kids who struggle?", "AI excels at gamifying learning, creating stories around educational content, and generating activities that match a child's specific interests. This personalization often re-engages students who found traditional schooling frustrating."),
        ("What if my child refuses to do schoolwork?", "Take a step back and reduce pressure. Focus on connection over compliance. Use AI to create micro-lessons (5-10 minutes) on topics they enjoy. Sometimes a break from formal learning helps reluctant learners reset."),
    ],
    '26-homeschool-assessment': [
        ("How do I know if my homeschooled child is on track?", "Use a combination of portfolio reviews, standardized test scores (if your state requires them), and regular narration or discussion to gauge understanding. AI can generate assessment questions aligned to grade-level standards."),
        ("Should I give my homeschooled child grades?", "Grades are optional for most homeschoolers unless your state requires them or your child plans to transfer to a traditional school. Many families prefer narrative evaluations or mastery-based progression."),
        ("What standardized tests can homeschoolers take?", "Homeschoolers commonly take the Iowa Assessments, Stanford Achievement Test (SAT-10), CAT/5, or state-specific assessments. High schoolers can take the PSAT, SAT, ACT, and AP exams."),
    ],
    '27-ai-history-alive': [
        ("How can AI make history more engaging for kids?", "AI can roleplay as historical figures for interviews, generate 'you are there' scenarios, create detailed timelines, and design project-based learning around historical events. This brings history from memorization to experience."),
        ("Can AI write historical fiction for homeschool?", "AI can create short historical fiction stories set in specific time periods, helping children experience history through narrative. Always fact-check the details and use these as starting points for deeper research."),
        ("What is the best way to teach history to homeschoolers?", "Combine living books, primary sources, hands-on projects, and AI-generated activities. Chronological study with a narrative spine (like Story of the World) supplemented by AI-designed projects works well for most families."),
    ],
    '28-best-free-resources': [
        ("What are the best free online resources for homeschooling?", "Top free resources include Khan Academy (math/science), ChatGPT and Claude free tiers (lesson planning), your local library system, PBS LearningMedia, CK-12 textbooks, MIT OpenCourseWare, and YouTube educational channels."),
        ("Can I homeschool completely free?", "Yes. Between library books, free online platforms, AI tools with free tiers, and community resources, you can provide a comprehensive education at no cost. The biggest investment is your time."),
        ("Are free homeschool resources as good as paid ones?", "Many free resources are equal to or better than paid alternatives. Khan Academy rivals expensive math programs, and AI tools provide personalized instruction that boxed curricula cannot match."),
    ],
    '29-ai-art-music-homeschool': [
        ("Can AI teach art and music to my kids?", "AI can generate art project ideas, explain techniques, create music theory lessons, and provide composition exercises. While it cannot replace hands-on practice, it is an excellent planning and inspiration tool."),
        ("How do I teach art if I'm not artistic?", "AI can provide step-by-step drawing tutorials, art history lessons, and creative project ideas tailored to your child's age. You do not need to be an artist yourself - you just need to provide materials and encouragement."),
        ("What music activities can AI generate for homeschool?", "AI can create rhythm exercises, music theory worksheets, listening guides for different genres, composer study plans, and even simple songwriting prompts. Pair these with free tools like Chrome Music Lab for hands-on practice."),
    ],
    '30-summer-learning-ai': [
        ("How do I prevent summer learning loss with AI?", "Use AI to create fun, low-pressure summer activities that maintain skills: reading challenges, nature journaling prompts, cooking math, and travel-based geography lessons. Keep it to 20-30 minutes daily."),
        ("Should homeschoolers take summer off?", "Most homeschool families take some kind of break but keep informal learning going. The beauty of homeschooling is flexibility - take time off when you need it and learn year-round at a relaxed pace when you want to."),
        ("What are good summer learning activities?", "Nature journals, cooking projects, garden math, library reading programs, science experiments, coding camps, and travel-based learning all keep kids engaged without feeling like formal school."),
    ],
    '31-college-admissions-homeschool': [
        ("Do homeschooled students get into good colleges?", "Yes. Homeschooled students are accepted at all types of colleges, including Ivy League schools. Many admissions officers report that homeschooled applicants stand out for their self-direction and unique experiences."),
        ("What do colleges want from homeschool applicants?", "Colleges want strong standardized test scores (SAT/ACT), a detailed transcript with course descriptions, letters of recommendation, a compelling personal essay, and evidence of extracurricular activities and community involvement."),
        ("When should homeschoolers start preparing for college?", "Begin planning in 9th grade: maintain detailed records, pursue dual enrollment or AP courses, prepare for standardized tests, and build a portfolio of activities. Start college visits and applications in 11th grade."),
    ],
    '32-ai-foreign-language': [
        ("Can AI teach my child a foreign language?", "AI is excellent for vocabulary, grammar, reading, and writing practice. For speaking and listening skills, supplement AI with language exchange apps, native speaker videos, and conversation practice with tutors or community members."),
        ("What languages can AI help teach?", "AI tools support all major world languages including Spanish, French, Mandarin, German, Japanese, Arabic, and many more. They can generate exercises, translate text, explain grammar rules, and create immersive scenarios."),
        ("At what age should kids start learning a second language?", "Earlier is better for language acquisition. Children under 10 have a natural advantage in developing native-like pronunciation. However, starting at any age is beneficial, and AI makes language learning accessible regardless of when you begin."),
    ],
    '33-ai-financial-literacy-kids': [
        ("How do I teach my kids about money?", "Start with basic concepts like earning, saving, and spending using real-world examples. AI can generate age-appropriate activities like running a pretend store, budgeting for a family meal, or understanding how interest works."),
        ("At what age should kids learn about financial literacy?", "Basic concepts like identifying coins and understanding that things cost money can start at age 4-5. By age 8-10, kids can learn about saving, budgeting, and basic investing concepts. Teens should understand credit, taxes, and compound interest."),
        ("What AI tools teach kids about money?", "ChatGPT and Claude can create custom financial literacy lessons, generate budgeting scenarios, and simulate business decisions. Pair AI instruction with real-world practice like managing a small allowance or tracking family expenses."),
    ],
    '34-homeschool-burnout': [
        ("How do I deal with homeschool burnout?", "Simplify your routine, lower your standards temporarily, outsource where possible (co-ops, online classes), and take a break without guilt. Remember that burned-out parents cannot teach effectively."),
        ("Is it normal to want to quit homeschooling?", "Absolutely. Most homeschool parents consider quitting at some point, usually during the first year or during major life transitions. Taking a short break and reassessing your approach often resolves the feeling."),
        ("How do I simplify homeschooling when overwhelmed?", "Cut back to the 'big three' (math, reading, writing) for a few weeks. Use AI to generate simple lesson plans so you do not have to plan from scratch. Add subjects back gradually as you recover."),
    ],
    '35-ai-coding-kids': [
        ("At what age can kids start learning to code?", "Children as young as 5-6 can begin with visual block-based coding (Scratch). By age 9-10, many kids are ready for text-based languages. AI can generate coding challenges and explain concepts at any level."),
        ("What programming language should kids learn first?", "Scratch (ages 5-9) for visual coding, then Python (ages 10+) as a first text-based language. Python has clear syntax and is widely used in AI and data science, making it a practical long-term choice."),
        ("How can AI help kids learn to code?", "AI can explain coding concepts in kid-friendly language, generate practice problems, debug code, and create project ideas. It acts as a patient tutor that can answer questions at any hour."),
    ],
    '36-unschool-ai': [
        ("What is unschooling?", "Unschooling is a child-led approach to education where learning happens naturally through play, exploration, and following the child's interests. There is no set curriculum, schedule, or required subjects."),
        ("How does AI work with unschooling?", "AI supports unschooling by helping parents follow their child's interests in real time. When a child asks about volcanoes, AI can instantly generate experiments, book recommendations, and project ideas on that topic."),
        ("Is unschooling legal?", "Unschooling is legal in all 50 states, though you must still comply with your state's homeschool laws regarding notification, record-keeping, and any required assessments."),
    ],
    '37-new-to-homeschool': [
        ("How do I start homeschooling?", "Check your state's homeschool laws, file any required paperwork, choose your approach (structured curriculum, interest-led, or somewhere in between), and start with the basics: reading, writing, and math."),
        ("Do I need a teaching degree to homeschool?", "No state requires a teaching degree to homeschool. Some states require a high school diploma or GED, but most have no educational requirements for homeschool parents at all."),
        ("How do I withdraw my child from public school?", "Requirements vary by state but generally involve writing a letter of intent to homeschool and submitting it to your local school district or state department of education. Some states require no notification at all."),
    ],
    '38-ai-physical-education': [
        ("How do homeschoolers get enough physical activity?", "Homeschool PE includes sports teams, martial arts, dance, swimming, cycling, hiking, and backyard play. Many communities have homeschool sports leagues, and AI can help design age-appropriate fitness routines."),
        ("Can AI design a PE curriculum for homeschool?", "AI can create age-appropriate workout plans, design obstacle courses, suggest sports drills, and plan active games. It can also track fitness goals and adapt activities based on your child's abilities and interests."),
        ("Do homeschoolers have to do PE?", "PE requirements vary by state. Even where not required, regular physical activity is essential for health and learning. Most homeschool families naturally incorporate more movement than traditional schools."),
    ],
    '39-dual-enrollment-guide': [
        ("What is dual enrollment for homeschoolers?", "Dual enrollment allows homeschool high school students to take college courses and earn both high school and college credit simultaneously. Most community colleges welcome homeschool students, and many courses are free or low-cost."),
        ("At what age can homeschoolers start dual enrollment?", "Most dual enrollment programs accept students starting at age 16 or during their junior year of high school. Some programs accept younger students who demonstrate academic readiness through placement tests."),
        ("Does dual enrollment save money on college?", "Yes, significantly. Dual enrollment credits are often free or cost $50-100 per course compared to $500-2,000+ per course at a four-year university. Some homeschoolers earn an associate's degree before graduating high school."),
    ],
    '40-what-alpha-school-gets-right-wrong': [
        ("What is Alpha School?", "Alpha School is a technology-focused private school that uses AI and personalized learning. Students complete core academic work in about 2 hours daily, then spend the rest of the day on workshops and projects."),
        ("Is Alpha School worth the cost?", "Alpha School tuition is significant (around $10,000-15,000/year). Many of its AI-powered learning methods can be replicated at home for free using tools like ChatGPT, Claude, and Khan Academy."),
        ("Can I replicate the Alpha School model at home?", "Yes. The core concept - using AI to compress academic instruction into 2 hours and freeing up time for projects - is achievable through homeschooling with AI tools at a fraction of the cost."),
    ],
    '41-ai-geography-lessons': [
        ("How can AI make geography fun for kids?", "AI can create virtual travel itineraries, generate 'guess the country' games, design map-based scavenger hunts, and build immersive scenarios where kids explore different regions and cultures through storytelling."),
        ("What are good geography activities for homeschool?", "Cooking international recipes, pen pal programs, virtual museum tours, map coloring, country research projects, and AI-generated travel planning activities all make geography engaging and hands-on."),
        ("Should I teach geography separately or integrate it?", "Integration works well. Combine geography with history (where events happened), science (climate and ecosystems), cooking (international cuisine), and reading (stories set in different countries) for deeper understanding."),
    ],
    '42-ai-report-cards': [
        ("Do homeschoolers need report cards?", "Report cards are not legally required in most states, but they are useful for tracking progress, motivating students, and providing documentation if your child later transfers to a traditional school or applies to college."),
        ("How do I grade homeschool work?", "You can use traditional letter grades, percentages, pass/fail, mastery-based assessment, or narrative evaluations. AI can help generate rubrics, grade written work, and create standardized assessments for any subject."),
        ("What should a homeschool report card include?", "Include the student's name, grading period, subjects studied, grades or evaluation, attendance (if required), and any special achievements. AI can format this into a professional-looking document."),
    ],
    '43-weekly-newsletter-sample': [
        ("What is the Skip School newsletter about?", "Skip School sends one email per week with practical AI homeschool tips, new tool reviews, copy-and-paste prompts, and real examples from homeschool families. It is free to subscribe."),
        ("How often does Skip School publish new content?", "Skip School publishes new articles and guides weekly, with a newsletter that goes out every week. The content covers AI tools, homeschool methods, curriculum planning, and state-specific guides."),
        ("Is the Skip School newsletter free?", "Yes, the Skip School newsletter is completely free. Subscribe at skipschool.ai/subscribe to receive weekly AI homeschool tips and resources directly in your inbox."),
    ],
    '44-ai-homeschool-myths': [
        ("Is it true that AI will make kids lazy?", "No. When used properly, AI encourages deeper thinking by freeing kids from rote tasks so they can focus on creativity, analysis, and problem-solving. The key is teaching kids to use AI as a tool, not a crutch."),
        ("Will AI replace human teachers?", "AI is a powerful supplement but not a replacement for human instruction. Parents provide the mentorship, emotional support, and real-world guidance that AI cannot replicate. AI handles the routine; you handle the relationship."),
        ("Is it cheating to use AI for homeschool?", "No. Using AI for homeschool is like using a calculator, encyclopedia, or textbook - it is a tool. The goal is learning, and AI helps you personalize and enhance that learning. What matters is how you use it."),
    ],
    '45-homeschool-schedule-templates': [
        ("What does a typical homeschool schedule look like?", "Most families do 3-4 hours of structured learning in the morning (math, reading, writing), followed by afternoon enrichment activities (science, art, music, PE). The exact schedule varies by family and age."),
        ("Should I follow a block schedule or traditional schedule?", "Block schedules (focusing on 1-2 subjects per day) work well for older students who need deep focus. Traditional schedules (multiple short subjects daily) suit younger students who benefit from variety."),
        ("How do I create a homeschool schedule that works?", "Start with your non-negotiables (meals, activities, work schedule), then fit in core subjects during your child's peak focus time. Build in breaks and flexibility. Adjust after 2 weeks based on what is working."),
    ],
    '46-ai-homeschool-faq': [
        ("Is AI homeschooling the same as online school?", "No. AI homeschooling uses AI as a tool within parent-directed education, while online school is a structured program with assigned teachers and schedules. AI homeschooling gives you much more flexibility and control."),
        ("Do I need to be tech-savvy to use AI for homeschool?", "No. If you can type a question and read the response, you can use AI for homeschooling. Tools like ChatGPT and Claude are designed to be conversational and easy to use, even for beginners."),
        ("Can AI replace a full homeschool curriculum?", "AI is best used alongside other resources rather than as a standalone curriculum. It excels at personalizing instruction, generating practice materials, and adapting to your child's needs, but you still guide the overall direction."),
    ],
    '47-ai-projects-by-age': [
        ("What AI projects are good for elementary students?", "For ages 5-10, try AI-generated story starters, science experiment ideas, art prompts, nature scavenger hunts, and simple coding activities with Scratch. Keep projects short and hands-on."),
        ("What AI projects work for middle schoolers?", "Ages 11-14 can tackle AI-designed research projects, creative writing with AI feedback, coding challenges, historical roleplays, debate preparation, and science fair project planning."),
        ("What AI projects suit high school students?", "High schoolers can work on AI-assisted essay writing (with AI as editor), advanced coding projects, business plan creation, college application prep, independent research, and AP exam study with AI tutoring."),
    ],
    '48-ai-homeschool-mistakes-first-year': [
        ("What is the biggest mistake new homeschoolers make?", "Trying to recreate school at home. Most new homeschoolers over-schedule, buy too much curriculum, and burn out within months. Start simple with 2-3 core subjects and add more as you find your rhythm."),
        ("How long does it take to adjust to homeschooling?", "Most families need 1-3 months to adjust, a period often called 'deschooling.' Children coming from traditional school may need time to decompress and rediscover their natural curiosity before structured learning resumes."),
        ("What should I avoid when starting to homeschool?", "Avoid buying expensive curriculum before trying free options, comparing your homeschool to others, over-scheduling, and expecting every day to go perfectly. Focus on building a sustainable routine that works for your family."),
    ],
    '49-bible-study-ai': [
        ("Can AI help with Bible study for kids?", "AI can generate discussion questions, create age-appropriate summaries of Bible stories, design craft activities related to lessons, and help plan a structured Bible curriculum. It is a planning tool, not a spiritual authority."),
        ("Is it appropriate to use AI for religious education?", "AI is a tool for lesson planning and resource generation, not a theological authority. Use AI to create engaging activities and discussion frameworks, but rely on your faith community and personal convictions for spiritual guidance."),
        ("What Bible curriculum works for homeschool?", "Popular options include Answers in Genesis, Apologia, Bible Study Guide for All Ages, and Grapevine Studies. AI can supplement any of these by generating additional discussion questions, activities, and review materials."),
    ],
    '50-eclectic-homeschool-ai': [
        ("What is eclectic homeschooling?", "Eclectic homeschooling means mixing and matching methods and resources from different approaches. You might use Charlotte Mason for reading, a traditional textbook for math, and unschooling for science. AI helps tie it all together."),
        ("How do I build an eclectic homeschool curriculum?", "Start with your child's needs and your family's values. Use AI to find the best resources from different methods for each subject. There is no single right way - the beauty of eclectic homeschooling is customization."),
        ("Is eclectic homeschooling effective?", "Yes. Eclectic homeschooling allows you to use whatever works best for each child and subject, making it highly personalized. AI makes it easier to manage the complexity of combining multiple approaches."),
    ],
    '51-montessori-ai': [
        ("What is Montessori homeschooling?", "Montessori homeschooling follows Maria Montessori's principles: child-led learning, hands-on materials, mixed-age interactions, prepared environments, and uninterrupted work periods. It emphasizes independence and intrinsic motivation."),
        ("How does AI fit into Montessori homeschooling?", "AI can help prepare the learning environment by suggesting appropriate activities, creating printable materials, and planning the progression of skills. It supports the guide (parent) without replacing the child-led nature of Montessori."),
        ("Do I need expensive Montessori materials?", "No. Many Montessori activities use common household items. AI can help you create DIY versions of Montessori materials and suggest practical life, sensorial, and academic activities using items you already have."),
    ],
    '52-ai-vocabulary-builder': [
        ("How can AI help build my child's vocabulary?", "AI can generate word lists at your child's level, create context-rich sentences, design vocabulary games, and produce reading passages that naturally introduce new words. It adapts difficulty based on progress."),
        ("How many new words should kids learn per week?", "Most literacy experts suggest 5-10 new vocabulary words per week for elementary students, with more for advanced readers. Focus on words encountered in actual reading rather than isolated word lists."),
        ("What is the best way to teach vocabulary?", "The most effective approach combines reading (encountering words in context), direct instruction (defining and discussing words), and repeated exposure (using words in conversation and writing). AI supports all three methods."),
    ],
    '53-homeschool-record-keeping': [
        ("What records do I need to keep for homeschool?", "Requirements vary by state. Common records include attendance logs, samples of student work, book/resource lists, standardized test results (if required), and course descriptions. Check your state's specific requirements."),
        ("How do I organize homeschool records?", "Use a simple system: a binder or digital folder for each school year containing attendance, completed work samples, book lists, and any required assessments. AI can generate templates and tracking spreadsheets."),
        ("Do I need to keep homeschool records if my state does not require them?", "Even if not legally required, keeping basic records protects you and helps with college applications, returning to public school, and documenting your child's educational history. Minimal record-keeping takes very little time."),
    ],
    '54-ai-handwriting-practice': [
        ("How can AI help with handwriting practice?", "AI can generate custom handwriting worksheets with your child's name, favorite words, or current vocabulary. It can create tracing sheets, copywork passages, and age-appropriate writing prompts that make practice more engaging."),
        ("At what age should kids start handwriting practice?", "Most children are ready for pre-writing activities (tracing, drawing shapes) at age 3-4 and formal letter formation at age 5-6. Focus on proper pencil grip and letter formation before speed or neatness."),
        ("Is cursive still worth teaching?", "Many educators believe cursive aids fine motor development, brain connectivity, and reading speed. It is still required in some states and useful for signatures. AI can generate cursive practice sheets tailored to your child's level."),
    ],
    '55-ai-test-prep': [
        ("Can AI help prepare for standardized tests?", "AI is excellent for test prep. It can generate practice questions in any subject, explain concepts in multiple ways, create timed practice sessions, and identify areas where your child needs additional review."),
        ("What standardized tests should homeschoolers prepare for?", "Common tests include the Iowa Assessments and Stanford Achievement Test for annual evaluation, PSAT and SAT/ACT for college-bound high schoolers, and AP exams for advanced credit."),
        ("How far in advance should we start test prep?", "For annual standardized assessments, 2-4 weeks of light review is usually sufficient for students who have been learning consistently. For college entrance exams like the SAT or ACT, 3-6 months of preparation is recommended."),
    ],
    '56-ai-debate-critical-thinking': [
        ("How does AI help teach critical thinking?", "AI can present multiple perspectives on an issue, generate counterarguments, ask Socratic questions, and create debate scenarios. This forces students to evaluate evidence, identify bias, and construct logical arguments."),
        ("At what age can kids start debating?", "Children can begin simple opinion-sharing and 'would you rather' discussions at age 6-7. By age 10-12, they can engage in structured debates. AI scales the complexity of debate topics to match maturity and skill level."),
        ("What are good debate topics for homeschool students?", "Start with familiar topics: 'Should kids have homework?' or 'Is it better to have a pet cat or dog?' Progress to current events, historical dilemmas, and ethical questions as students develop their reasoning skills."),
    ],
    '57-ai-learning-disabilities-detection': [
        ("Can AI detect learning disabilities?", "AI cannot diagnose learning disabilities, but it can help identify patterns that suggest further evaluation is needed. If your child consistently struggles in specific areas despite quality instruction, consult a professional for formal assessment."),
        ("What are signs my child might have a learning difference?", "Common signs include difficulty with reading despite practice, reversing letters past age 7, trouble with math concepts peers grasp easily, poor working memory, and significant gaps between verbal ability and written output."),
        ("Where can I get my homeschooled child evaluated?", "Contact your local school district (they must evaluate homeschooled children for free under IDEA), a private psychologist, or a pediatric neuropsychologist. Many offer virtual evaluations."),
    ],
    '58-homeschool-with-toddlers': [
        ("How do I homeschool with a toddler at home?", "Use independent play stations, schedule focused teaching during nap time, include toddlers in simple activities, and accept that some days will be chaotic. Short, flexible lessons work better than long structured blocks."),
        ("Should I include my toddler in homeschool activities?", "Yes, when possible. Toddlers can do simplified versions of art projects, listen to read-alouds, sort objects for math concepts, and explore sensory bins. This builds their learning foundation and prevents meltdowns from exclusion."),
        ("How do I keep a toddler busy while teaching older kids?", "Rotate special toys only available during school time, use sensory bins, set up a 'school station' with coloring and play-doh, and involve them in the lesson when possible. Planning 2-3 independent activities in advance is key."),
    ],
    '59-world-history-ai-unit': [
        ("How can AI help teach world history?", "AI can generate immersive scenarios, create timelines, roleplay as historical figures, design project-based lessons, and connect ancient events to modern parallels. It makes history active rather than passive."),
        ("What period should kids start learning history?", "Many curricula start with ancient civilizations (Egypt, Greece, Rome) and progress chronologically. Charlotte Mason and classical methods use a four-year cycle. The key is making history narrative-driven and engaging."),
        ("Can AI generate accurate historical content?", "AI is generally reliable for well-documented historical events but may contain errors in details or interpretation. Always cross-reference important facts with established sources and teach kids to verify AI-generated history."),
    ],
    '60-ai-executive-function': [
        ("What are executive function skills?", "Executive function skills include working memory, flexible thinking, self-control, time management, organization, and task initiation. These 'brain management' skills develop throughout childhood and are essential for academic success."),
        ("How can AI help develop executive function in kids?", "AI can create visual schedules, break complex tasks into small steps, generate checklists, set up routine structures, and provide scaffolded instructions. This external structure supports kids as their internal executive function develops."),
        ("Are executive function challenges the same as ADHD?", "Not necessarily. While ADHD involves executive function difficulties, many children without ADHD also have executive function challenges. These skills develop at different rates, and most children benefit from explicit instruction and practice."),
    ],
    '61-ai-stem-girls': [
        ("How do I encourage my daughter in STEM?", "Expose her to diverse STEM role models, frame challenges as learning opportunities rather than failures, use AI to create projects aligned with her interests, and avoid gendered language about who is 'good at math.'"),
        ("What AI tools are best for girls in STEM?", "All AI tools work equally well regardless of gender. The key is using AI to create personally relevant projects - if she loves animals, build a wildlife data project; if she loves art, explore computational art and design."),
        ("Why do girls lose interest in STEM?", "Research shows girls' STEM interest often drops around ages 11-13 due to social pressure and lack of relatable role models. Homeschooling provides an advantage by removing these peer pressures and allowing interest-led learning."),
    ],
    '62-ai-reading-comprehension': [
        ("How can AI improve reading comprehension?", "AI can generate pre-reading questions, create vocabulary previews, design during-reading check-ins, and produce post-reading discussion questions. It tailors comprehension activities to your child's specific reading level and interests."),
        ("What reading level should my child be at?", "Reading levels vary significantly among children of the same age. Focus on steady progress rather than grade-level benchmarks. AI can assess approximate reading level and suggest books at the right challenge point."),
        ("How do I help a child who reads but does not understand?", "Focus on visualization, summarization, and connection-making strategies. Have your child narrate what they read in their own words. AI can generate targeted comprehension exercises that build specific skills like inference and main idea identification."),
    ],
    '63-homeschool-dad-guide': [
        ("Can dads be the primary homeschool teacher?", "Absolutely. More fathers are becoming primary homeschool parents, and children benefit from the different perspectives and teaching styles dads bring. There is no reason the primary educator must be mom."),
        ("How do I homeschool while working full-time?", "Many working homeschool parents use a combination of morning/evening instruction, independent work during work hours, AI-generated self-directed lessons, co-ops, and flexible work arrangements."),
        ("What do homeschool dads wish they knew starting out?", "Common advice from experienced homeschool dads: do not try to be a school teacher, lower your expectations for the first few months, build relationship before rigor, and find a community of other homeschool parents."),
    ],
    '64-ai-nature-journal': [
        ("What is nature journaling?", "Nature journaling is the practice of observing and recording the natural world through writing, drawing, and scientific notes. It develops observation skills, scientific thinking, artistic ability, and a connection to the environment."),
        ("How can AI enhance nature journaling?", "AI can identify plants and animals from descriptions, suggest observation prompts, provide background information on species your child encounters, and generate follow-up research questions that deepen understanding."),
        ("What supplies do you need for a nature journal?", "A simple notebook, pencils, and colored pencils are all you need. Some families add a magnifying glass, field guides, and a camera. The focus is on observation and recording, not artistic perfection."),
    ],
    '65-gifted-homeschool-ai': [
        ("Is homeschooling good for gifted children?", "Homeschooling is often ideal for gifted children because it allows acceleration in strong areas, deeper exploration of interests, and a pace that matches their ability. AI makes acceleration and enrichment even more accessible."),
        ("How do I challenge a gifted child with AI?", "Use AI to generate advanced-level content, create open-ended projects, explore interdisciplinary connections, and provide college-level material in areas of strength. AI can adapt complexity in real time to keep gifted learners engaged."),
        ("Should I skip grades for my gifted child?", "Subject acceleration (advancing in specific subjects) is usually better than whole-grade skipping. This keeps social development on track while providing academic challenge. AI makes subject-level acceleration easy to implement."),
    ],
    '66-ai-grammar-painless': [
        ("How do I teach grammar without boring my kids?", "Use AI to turn grammar into games, create humorous example sentences, generate editing challenges with funny mistakes, and design grammar-based creative writing prompts. Context-based grammar beats worksheet drilling."),
        ("At what age should kids learn formal grammar?", "Basic grammar concepts (nouns, verbs, sentences) can start at age 6-7. Formal grammar instruction (parts of speech, sentence diagramming, complex punctuation) is most effective starting around age 9-10 when abstract thinking develops."),
        ("Is AI good at teaching grammar?", "AI is excellent for grammar instruction. It can explain rules with clear examples, generate practice sentences, check student writing for errors, and provide detailed feedback on grammar usage in context."),
    ],
    'ai-homeschool-complete-guide': [
        ("Is AI homeschooling right for my family?", "AI homeschooling works for most families because the AI adapts to any educational philosophy, budget, and schedule. If you have internet access and are willing to learn alongside your child, AI can enhance your homeschool."),
        ("How much does AI homeschooling cost?", "AI homeschooling can be completely free using tools like ChatGPT and Claude with their free tiers, Khan Academy, and library resources. Paid options typically run $20-40/month for premium AI tool access."),
        ("Do I need to be tech-savvy to homeschool with AI?", "No. Modern AI tools are designed to be conversational - you type a question, and you get a helpful answer. If you can send a text message, you can use AI for homeschooling."),
    ],
    'texas-esa-guide': [
        ("What is the Texas Education Freedom Account?", "The Texas Education Freedom Account (TEFA) is a state-funded program that provides money to eligible Texas families to use for qualified educational expenses, including homeschool curriculum, tutoring, and educational technology."),
        ("How much money do Texas ESA families receive?", "The exact amount varies by program year and eligibility. Check the Texas Education Agency website for current funding levels and application deadlines."),
        ("Can homeschoolers in Texas use ESA funds for AI tools?", "Educational technology and software are generally qualified expenses under ESA programs. AI tools used for educational purposes would typically qualify, but verify with the specific program guidelines."),
    ],
    'homeschool-kids-ai-five-years-ahead': [
        ("Will AI give homeschooled kids an advantage?", "Children who learn to use AI tools effectively develop skills in prompt engineering, critical evaluation, and human-AI collaboration that most traditionally schooled students will not gain until college or the workforce."),
        ("Is it too early to teach kids about AI?", "No. Children growing up today will live and work in an AI-driven world. Teaching them to use AI effectively and ethically now gives them a significant head start, regardless of their age."),
        ("What skills do AI-literate kids develop?", "AI-literate children develop critical thinking (evaluating AI output), clear communication (writing effective prompts), creativity (using AI as a collaborator), and metacognition (understanding how they learn best)."),
    ],
}

# HTML template for FAQ section
FAQ_SECTION_TEMPLATE = """
        <div class="faq-section" style="margin-top: 48px; padding-top: 32px; border-top: 2px solid #e8e4de;">
            <h2 style="font-family: 'Fraunces', serif; font-size: 28px; color: #0d203b; margin-bottom: 24px;">Frequently Asked Questions</h2>
{qa_blocks}
        </div>
"""

FAQ_QA_TEMPLATE = """            <div class="faq-item" style="margin-bottom: 20px; padding: 20px; background: #f8f6f2; border-radius: 10px; border: 1px solid #e8e4de;">
                <h3 style="font-family: 'Fraunces', serif; font-size: 18px; color: #0d203b; margin-bottom: 8px;">{question}</h3>
                <p style="color: #444; line-height: 1.7; margin: 0;">{answer}</p>
            </div>"""

def build_faq_schema(slug, qa_list):
    """Build FAQPage JSON-LD schema"""
    faq_entities = []
    for q, a in qa_list:
        faq_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })

    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_entities
    }

    return '    <script type="application/ld+json">\n    ' + json.dumps(schema, indent=4).replace('\n', '\n    ') + '\n    </script>'

modified = 0
skipped = 0

for slug, qa_list in faqs.items():
    filepath = os.path.join(SRC, slug + '.html')
    if not os.path.exists(filepath):
        print(f"  SKIP (not found): {slug}")
        skipped += 1
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'FAQPage' in content or 'faq-section' in content:
        print(f"  SKIP (already has FAQ): {slug}")
        skipped += 1
        continue

    # Build FAQ HTML
    qa_blocks = '\n'.join([FAQ_QA_TEMPLATE.format(question=q, answer=a) for q, a in qa_list])
    faq_html = FAQ_SECTION_TEMPLATE.format(qa_blocks=qa_blocks)

    # Build FAQ schema
    faq_schema = build_faq_schema(slug, qa_list)

    # Insert FAQ section before the related-articles div (or before </article> if no related)
    if '<div class="related-articles"' in content:
        content = content.replace('<div class="related-articles"', faq_html + '\n        <div class="related-articles"', 1)
    elif '</article>' in content:
        content = content.replace('</article>', faq_html + '\n    </article>', 1)
    else:
        print(f"  SKIP (no insertion point): {slug}")
        skipped += 1
        continue

    # Insert FAQ schema after existing schema script
    if '</script>' in content and 'application/ld+json' in content:
        # Find the first ld+json closing tag and insert after it
        schema_end = content.find('</script>', content.find('application/ld+json'))
        if schema_end != -1:
            insert_pos = schema_end + len('</script>')
            content = content[:insert_pos] + '\n' + faq_schema + content[insert_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    modified += 1
    print(f"  OK: {slug} (+{len(qa_list)} FAQs)")

print(f"\nDone: {modified} modified, {skipped} skipped")
