#!/usr/bin/env python3
"""Generate state ESA / school choice guide pages for 10+ states."""
import os, json

DEPLOY_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(DEPLOY_DIR)
SRC = os.path.join(ROOT, "site", "files", "src")

nav = open(os.path.join(DEPLOY_DIR, "nav_snippet.txt"), "r", encoding="utf-8").read()
footer = open(os.path.join(DEPLOY_DIR, "footer_snippet.txt"), "r", encoding="utf-8").read()

# ── State data ──────────────────────────────────────────────────────────
STATES = [
    {
        "slug": "florida-esa-guide",
        "state": "Florida",
        "abbr": "FL",
        "program_name": "Florida Family Empowerment Scholarship (FES)",
        "meta_title": "Florida ESA Guide for Homeschool Families 2026 | Skip School",
        "meta_desc": "Complete guide to Florida's Family Empowerment Scholarship for homeschool families. Eligibility, funding amounts, approved expenses, and how to apply.",
        "h1": "Florida ESA Guide for Homeschool Families",
        "subtitle": "Everything you need to know about the Family Empowerment Scholarship and how it works for Florida homeschoolers.",
        "intro": "Florida has one of the most expansive school choice programs in the country. The Family Empowerment Scholarship (FES) is now available to all Florida students regardless of income, making it one of the most accessible ESA programs nationwide. Here is what homeschool families need to know.",
        "amount": "Up to $8,000+ per student annually (varies by grade level and program track)",
        "eligibility": [
            "Any Florida resident student ages 5-18 (universal eligibility since 2023)",
            "Student must not be enrolled in a public school",
            "Student must be a Florida resident for the current school year",
            "No income cap for the universal track"
        ],
        "approved_expenses": [
            "Private school tuition and fees",
            "Textbooks and instructional materials",
            "Curriculum programs and online courses",
            "Tutoring services from approved providers",
            "Educational therapy services",
            "Standardized testing fees",
            "Part-time college tuition for eligible high school students",
            "Transportation to approved educational providers (up to a cap)"
        ],
        "how_to_apply": [
            "Visit the Step Up for Students website (stepupforstudents.org)",
            "Create a parent account and complete the online application",
            "Submit proof of Florida residency and student identification",
            "Select your Scholarship Funding Organization (SFO)",
            "Once approved, funds are loaded onto a ClassWallet spending account",
            "Submit receipts for approved purchases through the ClassWallet portal"
        ],
        "key_dates": "Applications open year-round. Most families apply before the school year begins in August. Processing typically takes 2-4 weeks.",
        "testing_req": "Students receiving FES funds must take an annual nationally norm-referenced assessment. Results are reported to the state but do not affect continued eligibility.",
        "tips": [
            "Apply early in the spring before the school year starts for smoother processing",
            "Keep all receipts organized digitally. ClassWallet requires documentation for every purchase",
            "Curriculum purchases from major providers like Khan Academy, IXL, and Outschool are generally approved",
            "AI tools like ChatGPT Plus subscriptions may qualify as instructional materials. Document how you use them in your curriculum"
        ],
        "faqs": [
            ("Can homeschool families use the FES in Florida?", "Yes. Florida's FES program covers homeschool families. You can use funds for curriculum materials, tutoring, online courses, and approved educational expenses. You do not need to enroll in a private school to use the scholarship."),
            ("How much does the Florida ESA pay homeschool families?", "The amount varies by grade level and program track but generally ranges from $7,000 to over $8,000 per student per year. Check the Step Up for Students website for the current year's exact amounts."),
            ("Do I have to take a standardized test for Florida's ESA?", "Yes, students receiving FES funds must take an annual nationally norm-referenced test. The results are reported to the state but do not determine continued eligibility. You choose from a list of approved assessments.")
        ]
    },
    {
        "slug": "arizona-esa-guide",
        "state": "Arizona",
        "abbr": "AZ",
        "program_name": "Arizona Empowerment Scholarship Account (ESA)",
        "meta_title": "Arizona ESA Guide for Homeschool Families 2026 | Skip School",
        "meta_desc": "Complete guide to Arizona's Empowerment Scholarship Account for homeschool families. Eligibility, funding amounts, approved expenses, and application steps.",
        "h1": "Arizona ESA Guide for Homeschool Families",
        "subtitle": "How to use Arizona's universal ESA program to fund your homeschool curriculum, tutoring, and educational materials.",
        "intro": "Arizona was the first state to make its ESA program universal in 2022, opening funding to all K-12 students regardless of income or prior school enrollment. The program gives families direct control over education spending through a dedicated account. Here is what homeschool families should know.",
        "amount": "Approximately $7,000 per student annually (adjusted each year based on state funding formula)",
        "eligibility": [
            "Any Arizona resident student eligible for K-12 education",
            "Student must not be simultaneously enrolled in a public school",
            "Must be an Arizona resident",
            "No income requirements (universal eligibility)"
        ],
        "approved_expenses": [
            "Curriculum and textbooks",
            "Online learning programs and courses",
            "Tutoring from certified or approved tutors",
            "Educational therapy and services for special needs",
            "Standardized testing and assessment fees",
            "Educational technology (computers, tablets for learning)",
            "Supplies for educational purposes",
            "Microschool or learning pod tuition"
        ],
        "how_to_apply": [
            "Visit the Arizona Department of Education ESA website",
            "Create a parent account on the ClassWallet platform",
            "Complete the online application with student and parent information",
            "Submit proof of Arizona residency",
            "Agree to the ESA contract terms",
            "Once approved, quarterly funds are deposited into your ClassWallet account"
        ],
        "key_dates": "Applications accepted year-round. Funds are distributed quarterly. Apply at least 30 days before you need funds to allow for processing.",
        "testing_req": "ESA students must take a nationally norm-referenced achievement test once per year. Results must be submitted to the Arizona Department of Education. There is no minimum score requirement.",
        "tips": [
            "Arizona allows ESA funds for educational technology, so a tablet or laptop for your child's learning is an approved expense",
            "Microschool and learning pod tuition is covered, making Arizona one of the most flexible ESA states",
            "Document everything. Take photos of materials, save digital receipts, and keep a log of how purchases support your curriculum",
            "Many families combine ESA funds with free resources like Khan Academy to stretch their budget further"
        ],
        "faqs": [
            ("Is Arizona's ESA available to all homeschool families?", "Yes. Since 2022, Arizona's ESA is universal. Any Arizona resident with a K-12 age child can apply regardless of income, prior school enrollment, or district. You do not need to have previously attended public school."),
            ("What can I buy with Arizona ESA funds?", "Approved expenses include curriculum, textbooks, online courses, tutoring, educational technology, standardized tests, and even microschool tuition. All purchases must be documented and directly tied to your child's education."),
            ("How often do I receive Arizona ESA funds?", "Funds are distributed quarterly into your ClassWallet account. The annual amount (approximately $7,000) is divided into four payments throughout the school year.")
        ]
    },
    {
        "slug": "west-virginia-esa-guide",
        "state": "West Virginia",
        "abbr": "WV",
        "program_name": "Hope Scholarship Program",
        "meta_title": "West Virginia Hope Scholarship Guide for Homeschool Families 2026 | Skip School",
        "meta_desc": "Complete guide to West Virginia's Hope Scholarship for homeschool families. Eligibility, funding, approved expenses, and how to apply for the WV ESA.",
        "h1": "West Virginia Hope Scholarship Guide for Homeschool Families",
        "subtitle": "How to use West Virginia's Hope Scholarship to fund curriculum, tutoring, and learning tools for your homeschool.",
        "intro": "West Virginia's Hope Scholarship is an education savings account program available to most WV students. Launched in 2022, the program provides direct funding families can use for a wide range of educational expenses. Here is what homeschool parents need to know.",
        "amount": "Approximately $4,600 per student annually",
        "eligibility": [
            "West Virginia resident students in grades K-12",
            "Student must have been enrolled in a WV public school for at least 45 days in the prior year (or be entering kindergarten/first grade)",
            "Certain exceptions apply for military families and students with disabilities",
            "No income cap"
        ],
        "approved_expenses": [
            "Curriculum and textbooks",
            "Online educational programs",
            "Tutoring services",
            "Educational supplies and materials",
            "Fees for standardized testing",
            "Educational software and technology",
            "Special needs therapy and services",
            "Summer educational programs"
        ],
        "how_to_apply": [
            "Visit the Hope Scholarship website (hopescholarshipwv.com)",
            "Create a parent account and submit an application",
            "Provide proof of WV residency and prior public school enrollment (if applicable)",
            "Review and sign the Hope Scholarship agreement",
            "Once approved, funds are disbursed through ClassWallet",
            "Use the funds for approved expenses and submit documentation"
        ],
        "key_dates": "Applications typically open in the spring for the following school year. Check the Hope Scholarship website for current deadlines.",
        "testing_req": "Hope Scholarship students must participate in an annual standardized assessment. Results are submitted to the Hope Scholarship Board but do not affect continued eligibility.",
        "tips": [
            "The 45-day public school enrollment requirement trips up many families. Plan ahead if you are transitioning from homeschool to Hope Scholarship",
            "Kindergarten and first-grade students are exempt from the prior enrollment requirement",
            "Keep detailed records of all purchases and how they relate to your educational plan",
            "Combine Hope Scholarship funds with free AI tools like ChatGPT and Claude to maximize your budget"
        ],
        "faqs": [
            ("Do I need to have been in public school to get the Hope Scholarship?", "In most cases, yes. Students must have been enrolled in a WV public school for at least 45 instructional days in the prior year. However, kindergartners, first graders, military-connected students, and students with disabilities may be exempt from this requirement."),
            ("How much does the WV Hope Scholarship pay?", "The Hope Scholarship provides approximately $4,600 per student per year. The exact amount is set annually based on state funding formulas."),
            ("Can I use Hope Scholarship money for online courses?", "Yes. Online educational programs, curriculum subscriptions, and digital learning platforms are approved expenses under the Hope Scholarship program.")
        ]
    },
    {
        "slug": "indiana-esa-guide",
        "state": "Indiana",
        "abbr": "IN",
        "program_name": "Indiana Choice Scholarship (Voucher) Program",
        "meta_title": "Indiana School Choice Guide for Homeschool Families 2026 | Skip School",
        "meta_desc": "Guide to Indiana's Choice Scholarship and ESA options for homeschool families. Eligibility, funding, and how Indiana homeschoolers can access education funding.",
        "h1": "Indiana School Choice Guide for Homeschool Families",
        "subtitle": "What Indiana homeschool families need to know about the Choice Scholarship program and available education funding options.",
        "intro": "Indiana has a well-established school choice voucher program that primarily serves private school families. While the voucher program itself requires private school enrollment, Indiana has been expanding education funding options. Here is what homeschool families should know about the current landscape.",
        "amount": "Voucher amounts vary by income tier, up to 90% of state tuition support (approximately $5,500-$7,000). Homeschool-specific ESA options are more limited.",
        "eligibility": [
            "For the Choice Scholarship: student must attend an eligible private school",
            "Income requirements vary by track (expanded income eligibility in recent years)",
            "Indiana resident students in grades K-12",
            "Homeschool families may access certain tax deductions for educational expenses"
        ],
        "approved_expenses": [
            "Private school tuition (Choice Scholarship)",
            "Indiana offers a tax deduction of up to $1,000 per child for homeschool educational expenses",
            "Curriculum and textbooks (via tax deduction)",
            "Educational software and materials (via tax deduction)",
            "Check current legislation for expanding ESA options"
        ],
        "how_to_apply": [
            "For the Choice Scholarship: apply through the Indiana Department of Education",
            "For homeschool tax deductions: claim on your Indiana state tax return",
            "Keep receipts for all educational expenses throughout the year",
            "Monitor Indiana legislature for new ESA legislation that may expand homeschool funding"
        ],
        "key_dates": "Choice Scholarship applications align with the school year. Tax deductions are claimed during annual tax filing. Check the Indiana DOE website for current timelines.",
        "testing_req": "Choice Scholarship students take the ILEARN assessment. Homeschool families in Indiana are not required to take standardized tests under current state law.",
        "tips": [
            "Indiana's primary voucher program requires private school enrollment, but the $1,000 per-child tax deduction is available to homeschoolers",
            "Keep all curriculum and educational supply receipts for your tax return",
            "Indiana has been actively considering ESA expansion. Stay informed through your local homeschool association",
            "Use free AI tools to supplement purchased curriculum and get the most from your education budget"
        ],
        "faqs": [
            ("Can Indiana homeschool families get a voucher?", "Indiana's Choice Scholarship voucher currently requires enrollment in an eligible private school. However, homeschool families can claim a state tax deduction of up to $1,000 per child for educational expenses. The legislature has been considering expanded ESA options."),
            ("What tax deductions do Indiana homeschoolers get?", "Indiana allows a state tax deduction of up to $1,000 per child for educational expenses including curriculum, textbooks, and educational software. This is claimed on your Indiana state tax return."),
            ("Is Indiana considering an ESA for homeschoolers?", "Indiana has seen multiple ESA bills introduced in recent legislative sessions. While the current voucher program focuses on private schools, there is growing momentum for broader education savings account options that would include homeschool families.")
        ]
    },
    {
        "slug": "north-carolina-esa-guide",
        "state": "North Carolina",
        "abbr": "NC",
        "program_name": "Opportunity Scholarship Program",
        "meta_title": "North Carolina ESA Guide for Homeschool Families 2026 | Skip School",
        "meta_desc": "Guide to North Carolina's Opportunity Scholarship and education funding for homeschool families. Eligibility, amounts, and how to apply.",
        "h1": "North Carolina Education Choice Guide for Homeschool Families",
        "subtitle": "What NC homeschool families need to know about the Opportunity Scholarship and education funding options.",
        "intro": "North Carolina offers the Opportunity Scholarship, which has expanded significantly in recent years. While primarily designed for private school tuition, the state has been broadening education choice options. Here is what NC homeschool families should know.",
        "amount": "Up to $7,468 per student for the Opportunity Scholarship (income-based tiers). Personal Education Savings Accounts (PESA) providing up to $3,000 for eligible families.",
        "eligibility": [
            "Opportunity Scholarship: NC resident, income eligibility requirements (expanding to universal by 2025-26)",
            "Student must attend an eligible nonpublic school for the voucher",
            "PESA accounts available for students with disabilities",
            "Homeschool families may benefit from expanding ESA legislation"
        ],
        "approved_expenses": [
            "Private school tuition and fees (Opportunity Scholarship)",
            "Curriculum and instructional materials (PESA)",
            "Tutoring and educational services (PESA)",
            "Assistive technology for students with disabilities (PESA)",
            "Standardized testing fees",
            "Educational therapy and related services"
        ],
        "how_to_apply": [
            "Opportunity Scholarship: apply through the NC State Education Assistance Authority (NCSEAA)",
            "PESA: apply through the NCSEAA website for eligible students with disabilities",
            "Submit income documentation and proof of NC residency",
            "Complete the application before posted deadlines"
        ],
        "key_dates": "Opportunity Scholarship applications typically open in January/February for the following school year. Check NCSEAA website for current deadlines.",
        "testing_req": "Opportunity Scholarship students at participating schools take nationally standardized tests. NC homeschool students must maintain nationally standardized test scores or have their school reviewed.",
        "tips": [
            "North Carolina's Opportunity Scholarship is moving toward universal eligibility, which may create more options for homeschool families in coming years",
            "The PESA program is specifically valuable for families with special needs children",
            "NC homeschool law requires annual standardized testing or evaluation. Use this requirement as a natural checkpoint in your curriculum planning",
            "Stay connected with the NC homeschool community for updates on ESA legislation"
        ],
        "faqs": [
            ("Can NC homeschoolers get the Opportunity Scholarship?", "The Opportunity Scholarship currently requires attendance at an eligible nonpublic school. Pure homeschool families cannot directly access the voucher. However, the PESA program is available for students with disabilities, and ESA legislation continues to evolve in North Carolina."),
            ("What is North Carolina's PESA program?", "The Personal Education Savings Account (PESA) provides up to $3,000 for students with disabilities to use on approved educational expenses including curriculum, tutoring, therapy, and assistive technology. It is administered through the NC State Education Assistance Authority."),
            ("Does North Carolina require homeschool testing?", "Yes. North Carolina requires homeschool students to take a nationally standardized achievement test annually. Results must be kept on file for at least one year but do not need to be submitted to the state unless requested.")
        ]
    },
    {
        "slug": "iowa-esa-guide",
        "state": "Iowa",
        "abbr": "IA",
        "program_name": "Students First Act (ESA Program)",
        "meta_title": "Iowa ESA Guide for Homeschool Families 2026 | Skip School",
        "meta_desc": "Complete guide to Iowa's Students First Act ESA for homeschool families. Eligibility, funding amounts, approved expenses, and how to apply.",
        "h1": "Iowa ESA Guide for Homeschool Families",
        "subtitle": "How Iowa's Students First Act provides education savings accounts for families choosing private or homeschool education.",
        "intro": "Iowa passed the Students First Act in 2023, creating a phased-in universal ESA program. By the 2025-26 school year, the program is open to all Iowa students regardless of income. Here is what homeschool families in Iowa need to know.",
        "amount": "Approximately $7,600 per student annually (based on state per-pupil funding)",
        "eligibility": [
            "Universal eligibility for all Iowa K-12 students (phased in, fully universal by 2025-26)",
            "Must be an Iowa resident",
            "Student must be enrolled in an accredited nonpublic school or approved homeschool program",
            "Homeschool families using competent private instruction (CPI) with reporting may be eligible"
        ],
        "approved_expenses": [
            "Private school tuition",
            "Textbooks and curriculum materials",
            "Online educational programs",
            "Tutoring services",
            "Educational technology and software",
            "Testing and assessment fees",
            "Fees for extracurricular academic programs"
        ],
        "how_to_apply": [
            "Apply through the Iowa Department of Education or designated administrator",
            "Complete the online ESA application with student and family information",
            "Provide proof of Iowa residency",
            "Indicate your education setting (nonpublic school or approved homeschool)",
            "Funds are disbursed to an education savings account for approved expenses"
        ],
        "key_dates": "Applications typically open in the spring before the school year. Check the Iowa Department of Education website for current deadlines and application windows.",
        "testing_req": "Iowa homeschool families using the ESA are subject to assessment requirements. Students may need to take standardized tests or provide portfolio-based evaluations depending on their homeschool designation.",
        "tips": [
            "Iowa distinguishes between different homeschool categories (CPI with or without reporting). Your ESA eligibility may depend on your classification",
            "The program phased in over three years. As of 2025-26, it is fully universal with no income restrictions",
            "Work with your local homeschool association to understand how the ESA interacts with Iowa's homeschool notification requirements",
            "Use ESA funds for quality curriculum and supplement with free AI tools for personalized instruction"
        ],
        "faqs": [
            ("Can Iowa homeschoolers use the ESA program?", "Iowa's Students First Act ESA is primarily structured around accredited nonpublic schools. Homeschool families using certain approved designations may be eligible. The rules vary based on your specific homeschool classification under Iowa law, so check with the Iowa Department of Education."),
            ("How much is the Iowa ESA worth?", "The Iowa ESA provides approximately $7,600 per student per year, based on the state's per-pupil funding formula. The exact amount is adjusted annually."),
            ("Is the Iowa ESA available to everyone now?", "Yes. After a three-year phase-in, the Iowa ESA became universally available in the 2025-26 school year. There are no income restrictions for the current application cycle.")
        ]
    },
    {
        "slug": "utah-esa-guide",
        "state": "Utah",
        "abbr": "UT",
        "program_name": "Utah Fits All Scholarship",
        "meta_title": "Utah ESA Guide for Homeschool Families 2026 | Skip School",
        "meta_desc": "Complete guide to Utah's Fits All Scholarship ESA for homeschool families. Eligibility, funding, approved expenses, and how to apply.",
        "h1": "Utah Fits All Scholarship Guide for Homeschool Families",
        "subtitle": "How Utah's universal education scholarship program helps homeschool families fund curriculum, tutoring, and educational materials.",
        "intro": "Utah launched the Fits All Scholarship in 2024, creating a universal education savings account for all Utah students. The program provides direct funding families can use for a variety of educational expenses. Here is what Utah homeschool families need to know.",
        "amount": "Approximately $8,000 per student annually",
        "eligibility": [
            "All Utah resident K-12 students",
            "No income requirements (universal program)",
            "Student must not be simultaneously enrolled full-time in a public school",
            "Must apply and be accepted into the program"
        ],
        "approved_expenses": [
            "Curriculum and textbooks",
            "Online courses and educational platforms",
            "Tutoring from approved providers",
            "Educational technology and devices",
            "Testing and assessment fees",
            "Specialized instruction and therapy",
            "Extracurricular educational programs",
            "Microschool or learning pod tuition"
        ],
        "how_to_apply": [
            "Visit the Utah Fits All website",
            "Create a family account and complete the online application",
            "Submit proof of Utah residency",
            "Accept the scholarship agreement terms",
            "Once approved, funds are loaded to your education spending account",
            "Use the funds for approved expenses and maintain documentation"
        ],
        "key_dates": "Applications open annually. Check the Utah Fits All website for current application windows and deadlines.",
        "testing_req": "Scholarship recipients must participate in an annual assessment. Utah offers multiple approved testing options for homeschool families.",
        "tips": [
            "Utah is one of the most homeschool-friendly ESA states. The Fits All Scholarship was designed with homeschool families in mind",
            "Microschool and learning pod expenses are covered, giving you flexibility in how you structure your child's education",
            "Start your application early. High demand means processing can take several weeks",
            "Pair ESA-funded curriculum with free AI tools to create a comprehensive, personalized learning experience"
        ],
        "faqs": [
            ("Is Utah's Fits All Scholarship available to homeschoolers?", "Yes. The Utah Fits All Scholarship is specifically designed to include homeschool families. You can use the funds for curriculum, online courses, tutoring, educational technology, and other approved educational expenses."),
            ("How much does the Utah Fits All Scholarship pay?", "The scholarship provides approximately $8,000 per student per year. The exact amount is determined annually based on state funding."),
            ("What testing is required for the Utah ESA?", "Students receiving the Fits All Scholarship must take an approved annual assessment. Utah offers several testing options for homeschool families, and results are used for program accountability but do not determine continued eligibility.")
        ]
    },
    {
        "slug": "ohio-esa-guide",
        "state": "Ohio",
        "abbr": "OH",
        "program_name": "EdChoice Scholarship Program",
        "meta_title": "Ohio School Choice Guide for Homeschool Families 2026 | Skip School",
        "meta_desc": "Guide to Ohio's EdChoice Scholarship and education funding options for homeschool families. Eligibility, amounts, and how Ohio homeschoolers can access funding.",
        "h1": "Ohio School Choice Guide for Homeschool Families",
        "subtitle": "What Ohio homeschool families need to know about the EdChoice Scholarship and available education funding.",
        "intro": "Ohio has multiple school choice programs, with the EdChoice Scholarship being the most prominent. While the primary voucher is for private school tuition, Ohio has been expanding its education options. Here is what homeschool families should know.",
        "amount": "EdChoice provides up to $6,166 (K-8) or $8,408 (9-12) per student. Jon Peterson Special Needs Scholarship provides up to $27,000 for students with disabilities.",
        "eligibility": [
            "EdChoice: expanded to near-universal eligibility for private school students",
            "Jon Peterson Scholarship: students with documented disabilities",
            "Ohio resident students in grades K-12",
            "Homeschool families can access the Jon Peterson Scholarship for special needs students"
        ],
        "approved_expenses": [
            "Private school tuition (EdChoice)",
            "Special education services and therapy (Jon Peterson)",
            "Assistive technology and specialized instruction (Jon Peterson)",
            "Curriculum and instructional materials for special needs students",
            "Related services outlined in the student's service plan"
        ],
        "how_to_apply": [
            "EdChoice: apply through the Ohio Department of Education scholarship portal",
            "Jon Peterson: work with your school district to establish an Individualized Service Plan",
            "Submit required documentation including proof of residency and disability documentation (if applicable)",
            "Check application deadlines on the Ohio DOE website"
        ],
        "key_dates": "EdChoice applications typically open in February. Jon Peterson applications follow the school district's timeline. Check the Ohio Department of Education for current dates.",
        "testing_req": "EdChoice students participate in required testing at their private schools. Ohio homeschool students must submit an annual academic assessment to their local superintendent.",
        "tips": [
            "Ohio's EdChoice is primarily for private school families, but the Jon Peterson Scholarship is a powerful option for homeschool families with special needs children",
            "The Jon Peterson Scholarship is one of the most generous special needs programs in the country at up to $27,000",
            "Ohio homeschool law requires annual notification and assessment. Stay compliant to maintain your homeschool status",
            "Monitor Ohio legislature for ESA expansion that may create direct homeschool funding options"
        ],
        "faqs": [
            ("Can Ohio homeschoolers get the EdChoice voucher?", "The EdChoice Scholarship requires enrollment in an eligible private school. Traditional homeschool families cannot directly access EdChoice. However, families with special needs children can use the Jon Peterson Special Needs Scholarship for educational services and therapy."),
            ("What is Ohio's Jon Peterson Scholarship?", "The Jon Peterson Special Needs Scholarship provides up to $27,000 per year for students with documented disabilities. Funds can be used for specialized instruction, therapy, assistive technology, and related services. Homeschool families with eligible students can access this program."),
            ("What are Ohio's homeschool requirements?", "Ohio requires parents to notify their local superintendent annually of their intent to homeschool. You must provide a curriculum outline and submit an annual academic assessment showing satisfactory progress.")
        ]
    },
    {
        "slug": "arkansas-esa-guide",
        "state": "Arkansas",
        "abbr": "AR",
        "program_name": "LEARNS Act (Education Freedom Account)",
        "meta_title": "Arkansas ESA Guide for Homeschool Families 2026 | Skip School",
        "meta_desc": "Complete guide to Arkansas's LEARNS Act education savings accounts for homeschool families. Eligibility, funding, approved expenses, and how to apply.",
        "h1": "Arkansas ESA Guide for Homeschool Families",
        "subtitle": "How the Arkansas LEARNS Act creates education freedom accounts for families choosing alternatives to public school.",
        "intro": "Arkansas passed the LEARNS Act in 2023, establishing one of the newest universal education savings account programs in the country. The program provides direct funding to families who opt out of public school. Here is what Arkansas homeschool families need to know.",
        "amount": "Approximately $6,600 per student annually (90% of state per-pupil foundation funding)",
        "eligibility": [
            "Arkansas resident students in grades K-12",
            "Universal eligibility (phased in, prioritizing lower-income families initially)",
            "Student must not be enrolled in a public school",
            "Must apply and be accepted into the program"
        ],
        "approved_expenses": [
            "Private school tuition",
            "Curriculum and textbooks",
            "Online educational programs and courses",
            "Tutoring services from approved providers",
            "Educational technology and devices",
            "Standardized testing and assessment fees",
            "Special needs services and therapy",
            "Transportation to educational providers"
        ],
        "how_to_apply": [
            "Visit the Arkansas Division of Elementary and Secondary Education (DESE) website",
            "Complete the Education Freedom Account application",
            "Submit proof of Arkansas residency and student identification",
            "Select your education plan (homeschool, private school, or hybrid)",
            "Once approved, funds are deposited into your education spending account"
        ],
        "key_dates": "The program launched in phases beginning in 2023-24. Check the Arkansas DESE website for current application windows and deadlines.",
        "testing_req": "Education Freedom Account students must participate in annual standardized testing. Arkansas provides approved testing options for homeschool families.",
        "tips": [
            "Arkansas's LEARNS Act is one of the most comprehensive school choice laws in the country",
            "Lower-income families receive priority in the initial phase-in. Check current eligibility tiers",
            "Document all educational expenses carefully. The program requires accountability for fund usage",
            "Combine ESA funds with free resources like Khan Academy and AI tools for a well-rounded curriculum"
        ],
        "faqs": [
            ("Can Arkansas homeschoolers use the LEARNS Act ESA?", "Yes. The LEARNS Act Education Freedom Account is available to homeschool families in Arkansas. You can use the funds for curriculum, online courses, tutoring, educational technology, and other approved expenses."),
            ("How much does the Arkansas ESA provide?", "The Education Freedom Account provides approximately $6,600 per student per year, which is 90% of the state's per-pupil foundation funding amount. The exact figure is adjusted annually."),
            ("When did Arkansas's ESA program start?", "The LEARNS Act was signed into law in March 2023. The Education Freedom Account program began rolling out in phases starting with the 2023-24 school year, with priority given to lower-income families.")
        ]
    },
    {
        "slug": "tennessee-esa-guide",
        "state": "Tennessee",
        "abbr": "TN",
        "program_name": "Education Savings Account Pilot Program",
        "meta_title": "Tennessee ESA Guide for Homeschool Families 2026 | Skip School",
        "meta_desc": "Guide to Tennessee's ESA pilot program and education funding options for homeschool families. Eligibility, current status, and what TN homeschoolers should know.",
        "h1": "Tennessee ESA Guide for Homeschool Families",
        "subtitle": "What Tennessee homeschool families need to know about the ESA pilot program and education choice options.",
        "intro": "Tennessee has been working on implementing an ESA program through its pilot program, which has faced legal challenges. The state continues to work toward expanded education choice. Here is the current state of play for Tennessee homeschool families.",
        "amount": "Pilot program provides approximately $7,000 per student for participating families in eligible counties.",
        "eligibility": [
            "Currently limited to students in Davidson and Shelby counties (Nashville and Memphis)",
            "Income-based eligibility requirements in the pilot phase",
            "Student must have attended a public school in an eligible district",
            "Tennessee is considering statewide expansion"
        ],
        "approved_expenses": [
            "Private school tuition at participating schools",
            "Tutoring from approved providers",
            "Textbooks and instructional materials",
            "Testing and assessment fees",
            "Educational supplies directly related to instruction",
            "Check program updates for expanded expense categories"
        ],
        "how_to_apply": [
            "Visit the Tennessee Department of Education ESA website",
            "Verify your county and income eligibility",
            "Complete the online application during the open window",
            "Submit required documentation (residency, income, prior enrollment)",
            "Selected families receive funds for approved educational expenses"
        ],
        "key_dates": "The pilot program has experienced delays due to legal challenges. Check the Tennessee DOE website for the latest application status and timelines.",
        "testing_req": "ESA participants must take state-approved assessments. Tennessee homeschool students follow their own assessment requirements under state homeschool law.",
        "tips": [
            "Tennessee's ESA program has faced significant legal challenges. Stay updated through the Tennessee DOE website",
            "Even without the ESA, Tennessee is one of the most homeschool-friendly states with minimal regulation",
            "Consider reaching out to Tennessee homeschool associations for the latest on ESA legislation",
            "Use free AI tools and open educational resources to build a strong curriculum while waiting for expanded funding options"
        ],
        "faqs": [
            ("Is Tennessee's ESA available to homeschoolers?", "Tennessee's current ESA pilot is limited to students in Davidson and Shelby counties who attend private schools. The program does not currently include homeschool families directly, but the state legislature has considered broader education choice options."),
            ("Which counties have the Tennessee ESA?", "The pilot program is currently limited to Davidson County (Nashville) and Shelby County (Memphis). Statewide expansion has been discussed but has not yet been implemented."),
            ("What are Tennessee's homeschool laws?", "Tennessee requires parents to notify their local school district of intent to homeschool. You must teach required subjects and maintain attendance records. Students in grades 5, 7, and 9 must take a standardized achievement test.")
        ]
    },
    {
        "slug": "oklahoma-esa-guide",
        "state": "Oklahoma",
        "abbr": "OK",
        "program_name": "Oklahoma Parental Choice Tax Credit / ESA Program",
        "meta_title": "Oklahoma School Choice Guide for Homeschool Families 2026 | Skip School",
        "meta_desc": "Guide to Oklahoma's school choice options for homeschool families. Tax credits, ESA programs, and education funding options for OK homeschoolers.",
        "h1": "Oklahoma School Choice Guide for Homeschool Families",
        "subtitle": "What Oklahoma homeschool families need to know about school choice tax credits and education funding options.",
        "intro": "Oklahoma has implemented school choice tax credits and has been exploring ESA legislation. The state already has one of the most permissive homeschool environments in the country. Here is what Oklahoma families should know about current and emerging funding options.",
        "amount": "Tax credit of up to $7,500 per student for private school tuition. Various amounts for other programs. Check current legislation for updated ESA amounts.",
        "eligibility": [
            "Oklahoma Parental Choice Tax Credit: available for private school expenses",
            "Oklahoma resident students in grades K-12",
            "Lindsey Nicole Henry Scholarship: for students with disabilities",
            "Various programs have different eligibility criteria"
        ],
        "approved_expenses": [
            "Private school tuition (tax credit)",
            "Special education services (Lindsey Nicole Henry Scholarship)",
            "Curriculum and textbooks (check current ESA legislation)",
            "Tutoring and educational services for students with disabilities",
            "Educational therapy and related services"
        ],
        "how_to_apply": [
            "Parental Choice Tax Credit: claimed on Oklahoma state tax return",
            "Lindsey Nicole Henry Scholarship: apply through the Oklahoma State Department of Education",
            "Keep receipts for all educational expenses",
            "Monitor Oklahoma legislature for new ESA legislation"
        ],
        "key_dates": "Tax credits are claimed during annual tax filing. Scholarship programs have specific application windows posted on the Oklahoma SDE website.",
        "testing_req": "Oklahoma homeschool students are not required to take standardized tests under current state law. Scholarship and ESA participants may have testing requirements specific to their program.",
        "tips": [
            "Oklahoma has some of the lightest homeschool regulations in the country. You do not need to register, test, or submit curriculum plans",
            "The Parental Choice Tax Credit can significantly offset private school costs. Explore hybrid homeschool/private school arrangements",
            "For students with disabilities, the Lindsey Nicole Henry Scholarship provides valuable funding for specialized services",
            "Oklahoma's legislature has been active on school choice. Stay informed about new ESA bills that may create direct homeschool funding"
        ],
        "faqs": [
            ("Does Oklahoma have an ESA for homeschoolers?", "Oklahoma does not currently have a standalone ESA program specifically for homeschoolers. However, the state offers a Parental Choice Tax Credit for private school expenses and the Lindsey Nicole Henry Scholarship for students with disabilities. ESA legislation continues to be considered."),
            ("What school choice options does Oklahoma have?", "Oklahoma offers the Parental Choice Tax Credit (up to $7,500 for private school tuition), the Lindsey Nicole Henry Scholarship for students with disabilities, and is actively considering broader ESA legislation."),
            ("Do Oklahoma homeschoolers need to test?", "No. Oklahoma does not require homeschool students to take standardized tests, submit curriculum plans, or register with the state. Oklahoma has some of the most minimal homeschool regulations in the country.")
        ]
    },
]


def build_page(s):
    elig_html = "\n".join(f"          <li>{e}</li>" for e in s["eligibility"])
    expenses_html = "\n".join(f"          <li>{e}</li>" for e in s["approved_expenses"])
    apply_html = "\n".join(f"          <li>{e}</li>" for e in s["how_to_apply"])
    tips_html = "\n".join(f"          <li>{t}</li>" for t in s["tips"])

    faq_schema_items = ",\n".join([
        f'''            {{
                "@type": "Question",
                "name": {json.dumps(q)},
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": {json.dumps(a)}
                }}
            }}''' for q, a in s["faqs"]
    ])

    faq_html_items = "\n".join([
        f'''        <div class="faq-item">
          <h3>{q}</h3>
          <p>{a}</p>
        </div>''' for q, a in s["faqs"]
    ])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{s["meta_title"]}</title>
  <meta name="description" content="{s["meta_desc"]}">
  <link rel="canonical" href="https://skipschool.ai/{s["slug"]}">
  <meta property="og:title" content="{s["meta_title"]}">
  <meta property="og:description" content="{s["meta_desc"]}">
  <meta property="og:url" content="https://skipschool.ai/{s["slug"]}">
  <meta property="og:type" content="article">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,700&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{s["h1"]}",
    "description": "{s["meta_desc"]}",
    "author": {{
      "@type": "Person",
      "name": "Ashley Larkin",
      "url": "https://skipschool.ai/about-ashley-larkin"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "Skip School",
      "url": "https://skipschool.ai"
    }},
    "datePublished": "2026-03-07",
    "dateModified": "2026-03-07"
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
{faq_schema_items}
    ]
  }}
  </script>
  <style>
    :root {{
      --navy: #0d203b;
      --yellow: #fbc926;
      --cream: #fdf8ef;
      --text: #1a1a1a;
      --muted: #5a5a5a;
      --border: #e5e5e5;
      --radius: 12px;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: "DM Sans", sans-serif; color: var(--text); background: var(--cream); line-height: 1.7; }}
    h1, h2, h3 {{ font-family: "Fraunces", serif; }}

    .esa-hero {{
      background: var(--navy);
      color: #fff;
      padding: 60px 20px;
      text-align: center;
    }}
    .esa-hero .container {{ max-width: 800px; margin: 0 auto; }}
    .esa-hero .breadcrumb {{ font-size: 0.9rem; margin-bottom: 16px; opacity: 0.7; }}
    .esa-hero .breadcrumb a {{ color: var(--yellow); text-decoration: none; }}
    .esa-hero h1 {{ font-size: 2.2rem; margin-bottom: 12px; }}
    .esa-hero .subtitle {{ font-size: 1.1rem; opacity: 0.9; max-width: 600px; margin: 0 auto 20px; }}
    .esa-hero .state-badge {{
      display: inline-block; background: var(--yellow); color: var(--navy);
      padding: 8px 20px; border-radius: 20px; font-weight: 700; font-size: 0.95rem;
    }}

    .esa-body {{ max-width: 800px; margin: 0 auto; padding: 48px 20px 60px; }}

    .info-card {{
      background: #fff; border: 1px solid var(--border); border-radius: var(--radius);
      padding: 28px; margin-bottom: 32px;
    }}
    .info-card h2 {{ font-size: 1.4rem; color: var(--navy); margin-bottom: 12px; }}
    .info-card p {{ margin-bottom: 12px; font-size: 1.02rem; }}
    .info-card ul {{ padding-left: 20px; margin-bottom: 12px; }}
    .info-card li {{ margin-bottom: 8px; font-size: 1rem; }}

    .amount-highlight {{
      background: linear-gradient(135deg, var(--navy), #1a3a6a);
      color: #fff; border-radius: var(--radius);
      padding: 24px 28px; margin-bottom: 32px;
      display: flex; align-items: center; gap: 16px;
    }}
    .amount-highlight .dollar {{ font-size: 2rem; }}
    .amount-highlight .amount-text h3 {{ font-size: 1.1rem; margin-bottom: 4px; color: var(--yellow); }}
    .amount-highlight .amount-text p {{ font-size: 0.95rem; opacity: 0.9; }}

    .section-title {{
      font-size: 1.5rem; color: var(--navy); margin: 40px 0 16px;
      padding-bottom: 8px; border-bottom: 3px solid var(--yellow);
      display: inline-block;
    }}

    .faq-section {{ margin-top: 48px; }}
    .faq-item {{
      background: #fff; border: 1px solid var(--border); border-radius: var(--radius);
      padding: 24px; margin-bottom: 16px;
    }}
    .faq-item h3 {{ font-size: 1.1rem; color: var(--navy); margin-bottom: 8px; }}
    .faq-item p {{ color: var(--muted); font-size: 0.98rem; }}

    .cta-box {{
      background: var(--navy); color: #fff; border-radius: var(--radius);
      padding: 36px; text-align: center; margin-top: 48px;
    }}
    .cta-box h2 {{ font-size: 1.4rem; margin-bottom: 10px; color: #fff; }}
    .cta-box p {{ margin-bottom: 18px; opacity: 0.9; }}
    .cta-box a {{
      display: inline-block; background: var(--yellow); color: var(--navy);
      padding: 12px 28px; border-radius: 8px; font-weight: 700;
      text-decoration: none; font-size: 1rem; margin: 4px 8px;
    }}

    .related-links {{
      margin-top: 40px; padding: 24px; background: #fff;
      border: 1px solid var(--border); border-radius: var(--radius);
    }}
    .related-links h3 {{ font-size: 1.1rem; color: var(--navy); margin-bottom: 12px; }}
    .related-links a {{
      display: inline-block; color: var(--navy); font-weight: 500;
      text-decoration: none; border-bottom: 2px solid var(--yellow);
      margin-right: 20px; margin-bottom: 8px;
    }}

    @media (max-width: 600px) {{
      .esa-hero h1 {{ font-size: 1.7rem; }}
      .amount-highlight {{ flex-direction: column; text-align: center; }}
    }}
  </style>
</head>
<body>
{nav}

  <section class="esa-hero">
    <div class="container">
      <div class="breadcrumb"><a href="/">Home</a> &raquo; <a href="/guides-index">Guides</a> &raquo; {s["state"]} ESA</div>
      <h1>{s["h1"]}</h1>
      <p class="subtitle">{s["subtitle"]}</p>
      <span class="state-badge">{s["state"]} ({s["abbr"]})</span>
    </div>
  </section>

  <div class="esa-body">

    <div class="amount-highlight">
      <div class="dollar">&#128176;</div>
      <div class="amount-text">
        <h3>Funding Amount</h3>
        <p>{s["amount"]}</p>
      </div>
    </div>

    <div class="info-card">
      <h2>Program Overview</h2>
      <p><strong>Program:</strong> {s["program_name"]}</p>
      <p>{s["intro"]}</p>
    </div>

    <h2 class="section-title">Eligibility Requirements</h2>
    <div class="info-card">
      <ul>
{elig_html}
      </ul>
    </div>

    <h2 class="section-title">Approved Expenses</h2>
    <div class="info-card">
      <p>Here is what you can use {s["state"]} ESA or scholarship funds for:</p>
      <ul>
{expenses_html}
      </ul>
    </div>

    <h2 class="section-title">How to Apply</h2>
    <div class="info-card">
      <ol style="padding-left:20px;">
{"".join(f"        <li style='margin-bottom:8px;'>{step}</li>{chr(10)}" for step in s["how_to_apply"])}
      </ol>
      <p style="margin-top:12px;"><strong>Key Dates:</strong> {s["key_dates"]}</p>
    </div>

    <h2 class="section-title">Testing Requirements</h2>
    <div class="info-card">
      <p>{s["testing_req"]}</p>
    </div>

    <h2 class="section-title">Tips for Homeschool Families</h2>
    <div class="info-card">
      <ul>
{tips_html}
      </ul>
    </div>

    <div class="faq-section">
      <h2 class="section-title">Frequently Asked Questions</h2>
{faq_html_items}
    </div>

    <div class="related-links">
      <h3>Related Guides</h3>
      <a href="/texas-esa-guide">Texas ESA Guide</a>
      <a href="/23-state-homeschool-laws">Homeschool Laws by State</a>
      <a href="/ai-homeschool-complete-guide">Complete AI Homeschool Guide</a>
      <a href="/11-homeschool-on-budget">Homeschool on a Budget</a>
    </div>

    <div class="cta-box">
      <h2>Get Weekly AI Homeschool Tips</h2>
      <p>Stay updated on ESA programs, AI tools, and curriculum ideas for your homeschool.</p>
      <a href="/subscribe">Subscribe Free</a>
      <a href="/guides-index" style="background:transparent;border:2px solid var(--yellow);color:var(--yellow);">Browse All Guides</a>
    </div>

  </div>

{footer}
</body>
</html>'''


for s in STATES:
    html = build_page(s)
    outpath = os.path.join(SRC, f"{s['slug']}.html")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created: {s['slug']}.html")

print(f"\nDone! Created {len(STATES)} state ESA guide pages.")
