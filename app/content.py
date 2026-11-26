# -*- coding: utf-8 -*-
"""All site content lives here as plain Python data structures.

This is a replica/homage of the Maverick Consulting Group (mcg-asia.com)
website, rebuilt as a self-contained Flask application.
"""

SITE = {
    "name": "Maverick Consulting Group",
    "short": "MCG",
    "tagline": "Government Relations, Public Affairs & Business Diplomacy",
    "email": "contact@mcg-asia.com",
    "address": "Dusit Central Park Offices, 946 Rama IV Road, Silom, Bangkok, Thailand",
    "year": 2026,
}

# Top navigation. Items with "children" render as dropdown folders.
NAV = [
    {"label": "HOME", "url": "/"},
    {
        "label": "OUR SERVICES",
        "children": [
            {"label": "Public Affairs & Government Relations", "url": "/services/public-affairs-government-relations"},
            {"label": "Political Risk & Intelligence", "url": "/services/political-risk-strategic-intelligence"},
            {"label": "Business Diplomacy & Market Expansion", "url": "/services/business-diplomacy-global-market-expansion"},
            {"label": "Strategic Communications & PR", "url": "/services/strategic-communications-public-relations"},
            {"label": "BOI & Business Setup", "url": "/services/boi-business-setup"},
            {"label": "Public Sector Solutions", "url": "/services/public-sector-advisory"},
        ],
    },
    {
        "label": "OUR EXPERIENCES",
        "children": [
            {"label": "Case Studies", "url": "/case-studies"},
            {"label": "Our Expertise", "url": "/our-expertise"},
        ],
    },
    {"label": "OUR TEAM", "url": "/our-team"},
    {"label": "MCG ARABIA", "url": "/mcg-arabia"},
    {"label": "FEATURED INSIGHTS", "url": "/featured-insights"},
]

HOME = {
    "hero_title": "Government Relations, Public Affairs & Business Diplomacy",
    "hero_intro": (
        "Maverick Consulting Group (MCG) is a Bangkok-based strategic advisory firm "
        "specialising in government relations, public affairs and business diplomacy. "
        "We advise governments, investors and multinational companies on regulatory "
        "strategy, policy engagement and market entry across Thailand and international markets."
    ),
    "future_ready_title": "Are You Future-Ready?",
    "future_ready_body": (
        "MCG goes beyond conventional public affairs and government relations consulting. "
        "Drawing on local expertise and an international network of strategic partners, we "
        "help organisations understand political and regulatory environments, anticipate "
        "policy developments and navigate complex stakeholder relationships. Our approach "
        "combines political and economic intelligence, strategic communications and "
        "stakeholder engagement to inform policy advocacy, build strategic partnerships, "
        "address regulatory challenges and facilitate market entry. We work with governments, "
        "multinational corporations, investors and industry associations operating in highly "
        "regulated and politically complex markets. Our focus is on developing credible "
        "strategies, building lasting relationships and creating the conditions for "
        "sustainable growth."
    ),
    "services_intro": (
        "At MCG, we understand that every business is unique. We leverage our consultants' "
        "diverse expertise to craft bespoke solutions that address your specific challenges."
    ),
    "expertise_intro": (
        "Bridge the Gap. MCG delivers comprehensive solutions, resolving complex client "
        "challenges through expert consulting and strategic partnerships. Our experienced "
        "consultants provide in-depth analysis and tailored strategies for market entry, "
        "compliance, investment optimisation, public affairs, government relations, public "
        "policy, and advocacy campaigns in Thailand."
    ),
}

# Six core services. Each has a landing page under /services/<slug>.
SERVICES = [
    {
        "slug": "public-affairs-government-relations",
        "title": "Public Affairs & Government Relations",
        "card_title": "Public Affairs & Government Relations",
        "tagline": "Protecting Interests, Inspiring Changes",
        "lead": (
            "We specialise in government relations and advocacy, ensuring your interests are "
            "represented and driving impactful policy change through strategic policy analysis "
            "and stakeholder engagement."
        ),
        "body": [
            "We help you understand complex government power plays and crack bureaucracy, "
            "navigating the intricacies of the political system, creating a levelled playing "
            "field, and raising the bar, while ensuring full transparency, business integrity, "
            "and good governance.",
            "At MCG, we advise multinational conglomerates to lead their industries and startups "
            "to design future-looking policies with strategic and impactful public affairs and "
            "government relations strategy that ensures all voices are heard and your objectives "
            "are achieved. Our proactive approach allows us to manage critical relationships with "
            "policymakers, regulators, and government stakeholders, ensuring you are first to know "
            "of key developments and preventing regulatory surprises.",
            "Our approach goes beyond traditional lobbying. We combine in-depth policy analysis "
            "with proactive stakeholder engagement to understand the intricacies of the political "
            "environment and develop tailored strategies that resonate with key decision-makers.",
        ],
        "scopes_title": "Explore some of Our PA/GR Scopes of Work",
        "scopes": [
            ("Government Relations Strategy & Advisory", "Developing government engagement strategies, identifying institutional priorities and advising on public-sector relationships relevant to business objectives."),
            ("Public Policy Advocacy & Representation", "Developing evidence-based policy positions, consultation submissions and advocacy strategies to support legitimate participation in policymaking and regulatory discussions."),
            ("Regulatory Affairs & Government Approvals", "Advising on regulatory pathways, licensing requirements, government approvals and administrative obstacles affecting business operations and investments."),
            ("Stakeholder Engagement & Coalition Building", "Designing and coordinating engagement with government bodies, industry associations, business coalitions and other relevant stakeholders around shared policy objectives."),
            ("Government Affairs Secretariat & Representation", "Providing ongoing government affairs support, coordinating institutional engagement, preparing policy submissions and supporting organisations without dedicated in-country public affairs teams."),
            ("Strategic Partnerships & Public\u2013Private Collaboration", "Identifying and developing strategic partnerships with governments and public institutions, supporting public\u2013private initiatives and structuring institutional cooperation."),
            ("Issues Management & Regulatory Response", "Developing strategic responses to emerging policy disputes, adverse regulatory developments and government-related issues affecting commercial interests."),
        ],
    },
    {
        "slug": "political-risk-strategic-intelligence",
        "title": "Political Risk & Strategic Intelligence",
        "card_title": "Political Risk & Strategic Intelligence",
        "tagline": "Anticipate. Assess. Advise.",
        "lead": (
            "Understanding political uncertainty, anticipating policy change and informing "
            "strategic decisions in complex markets."
        ),
        "body": [
            "Political developments can reshape markets, investment conditions and commercial "
            "interests. Geopolitical tensions, regulatory intervention, government transitions "
            "and shifting economic priorities create risks and opportunities that extend beyond "
            "immediate political events.",
            "Maverick Consulting Group (MCG) provides political risk advisory and strategic "
            "intelligence to businesses, investors and institutions navigating complex "
            "international markets. Our analysis goes beyond political developments to examine the "
            "institutions, economic interests and regulatory frameworks shaping government decisions.",
            "By combining geopolitical analysis, political and economic intelligence, and "
            "institutional understanding, MCG helps organisations anticipate risks, evaluate "
            "opportunities and make informed decisions in uncertain environments.",
        ],
        "scopes_title": "Explore Our Scope of Work",
        "scopes": [
            ("Political & Country Risk Assessment", "Assessing political stability, geopolitical exposure, policy uncertainty and risks affecting business operations, investments and market access."),
            ("Policy & Regulatory Intelligence", "Monitoring political developments, government priorities, legislative changes and emerging regulatory issues to identify risks and opportunities."),
            ("Stakeholder & Power Mapping", "Identifying key stakeholders, assessing institutional authority and influence dynamics, and mapping decision-making relationships relevant to policy and commercial interests."),
            ("Political & Regulatory Due Diligence", "Assessing the political, institutional and regulatory environment surrounding proposed investments, market entry, transactions and commercial partnerships."),
            ("Scenario Planning & Strategic Foresight", "Developing plausible political, economic and geopolitical scenarios to assess potential consequences and inform long-term strategic decisions."),
            ("Monitoring & Early Warning", "Ongoing monitoring of political, geopolitical and regulatory developments, with tailored alerts and executive briefings on emerging risks."),
        ],
    },
    {
        "slug": "business-diplomacy-global-market-expansion",
        "title": "Business Diplomacy & Global Market Expansion",
        "card_title": "Business Diplomacy & Global Market Expansion",
        "tagline": "Global Business Diplomacy: Market Access & Investment",
        "lead": (
            "Unlock international opportunities with our expert market research, investment "
            "advisory, and strategic partnerships."
        ),
        "body": [
            "We leverage robust relationships with embassies, influential business leaders, and "
            "government stakeholders, coupled with an extensive network of local and international "
            "consultants worldwide. We don\u2019t believe in arranged marriages. While others "
            "guarantee a shotgun wedding, we equip you with all possible insights and support so "
            "you can make informed decisions.",
            "Successful international market expansion demands strategic business diplomacy, "
            "in-depth understanding of global markets, and access to key influencers. We guide "
            "clients in maximising available government benefits and aligning their business "
            "strategies with the country's broader development policies, ensuring long-term "
            "sustainability and fostering positive relationships with host nations.",
            "Whether you seek to enter new markets, attract foreign investment, or build strategic "
            "global alliances, MCG's business diplomacy experts provide the guidance and "
            "connections you need.",
        ],
        "scopes_title": "Explore some of Our Scopes of Work",
        "scopes": [
            ("International Market Entry & Expansion", "Developing market-entry strategies, assessing commercial opportunities and supporting business establishment and expansion across international markets."),
            ("Foreign Investment Advisory & Facilitation", "Advising on cross-border investment opportunities, investment promotion frameworks, government incentives and institutional requirements affecting foreign investors."),
            ("Strategic Partnerships & Business Matching", "Identifying prospective commercial partners, evaluating strategic fit and facilitating cross-border business relationships, joint ventures and institutional partnerships."),
            ("Commercial & Non-Financial Due Diligence", "Assessing prospective partners, market conditions, institutional considerations and non-financial risks associated with international transactions and investments."),
            ("Trade Missions & Investment Delegations", "Designing and coordinating international business missions, investment delegations and structured engagement programmes."),
            ("Embassy & Institutional Engagement", "Supporting engagement with embassies, investment promotion agencies, chambers of commerce and international business institutions to advance cross-border cooperation."),
        ],
    },
    {
        "slug": "strategic-communications-public-relations",
        "title": "Strategic Communications & Public Relations",
        "card_title": "Strategic Communications & Public Relations",
        "tagline": "We don't just do PR. We engineer influence.",
        "lead": (
            "Craft powerful public advocacy campaigns, secure media coverage, design memorable "
            "experiences, establish executive thought leadership, and strengthen your corporate "
            "branding and positioning."
        ),
        "body": [
            "Forget surface-level communications. We build strategic, integrated campaigns that "
            "shape perception, build reputation and move stakeholders to action across media, "
            "policy and public audiences.",
            "We combine corporate messaging, media relations, executive positioning and crisis "
            "preparedness to make sure your organisation's story is clear, credible and "
            "consistently told to the audiences that matter most.",
        ],
        "scopes_title": "Explore some of Our Scopes of Work",
        "scopes": [
            ("Corporate Positioning & Strategic Messaging", "Developing corporate narratives, communications strategies and key messages aligned with business objectives and stakeholder expectations."),
            ("Media Relations & Campaigns", "Managing media engagement, press relations, editorial opportunities and targeted media campaigns to strengthen visibility and communicate key messages."),
            ("Media Monitoring & Intelligence", "Monitoring media coverage, public narratives and emerging issues, with analysis of media sentiment, reputational exposure and developments requiring attention."),
            ("Public Engagement & Strategic Events", "Designing and delivering public engagement programmes, conferences, exhibitions, forums, roundtables and stakeholder events."),
            ("Crisis Communications & Reputation Management", "Developing crisis communications strategies, managing sensitive public issues and coordinating media and stakeholder responses during reputational challenges."),
            ("Executive Communications & Thought Leadership", "Developing executive positioning, speeches, opinion pieces, leadership narratives and thought leadership programmes."),
        ],
    },
    {
        "slug": "boi-business-setup",
        "title": "BOI & Investment Promotion Advisory",
        "card_title": "BOI & Investment Promotion Advisory",
        "tagline": "Set up, scale up, and unlock government incentives.",
        "lead": (
            "We guide investors through BOI promotion, company incorporation and licensing so you "
            "can establish and grow your business in Thailand with confidence."
        ),
        "body": [
            "Thailand's Board of Investment (BOI) offers significant incentives to qualifying "
            "businesses, from tax holidays and import duty exemptions to relaxed foreign ownership "
            "and streamlined work permits. MCG helps you understand eligibility, structure your "
            "application, and secure the privileges that fit your business.",
            "From company registration to post-approval compliance, we provide end-to-end support "
            "so that your market entry is smooth, compliant and aligned with national development "
            "priorities.",
        ],
        "scopes_title": "Frequently Asked Questions",
        "scopes": [
            ("Can a BOI-promoted company own land in Thailand?", "A BOI-promoted company may be permitted to own land for carrying out the approved business activity, subject to size limitations, location requirements, and specific BOI approval. Land ownership is not automatic."),
            ("Does BOI promotion allow 100% foreign ownership?", "In certain approved cases, BOI promotion may permit 100 percent foreign ownership of a company, notwithstanding restrictions under general foreign business regulations. This depends on the approved business activity and conditions imposed by the BOI."),
            ("Does BOI promotion facilitate work permits and visas?", "BOI promotion streamlines the process of obtaining work permits and visas for foreign employees and specialists through the One Stop Service Center, subject to approved positions and conditions."),
            ("What tax incentives are available?", "Eligible activities may enjoy corporate income tax exemptions, import duty exemptions on machinery and raw materials, and other non-tax privileges depending on the activity and location."),
        ],
    },
    {
        "slug": "public-sector-advisory",
        "title": "Public Sector Solutions",
        "card_title": "Public Sector Advisory & Solutions",
        "tagline": "Shape the Future. Drive Real Impact.",
        "lead": (
            "Strategic support for governments, public organisations, and embassies. We deliver "
            "creative solutions for effective country branding, international events, executive "
            "training, strategic partnerships, and public engagement campaigns."
        ),
        "body": [
            "MCG understands the intricacies of public sector operations, the importance of "
            "effective international relations, the need for impactful communication strategies, "
            "and real-world execution that resonates with all stakeholders.",
            "We provide strategic advisory and institutional support to governments, diplomatic "
            "missions, international organisations, chambers of commerce and business associations. "
            "Our work spans public policy, institutional development, economic diplomacy and the "
            "management of cross-sector initiatives that connect public and private interests.",
        ],
        "scopes_title": "Explore some of Our Public Sector Offerings",
        "scopes": [
            ("Public Policy & Government Advisory", "Providing strategic advice on public policy development, government priorities, policy implementation and institutional decision-making."),
            ("Institutional Development & Capacity Building", "Supporting institutional assessments, organisational development, governance improvement and capacity-building programmes for public-sector organisations."),
            ("Institutional Representation & Secretariat Services", "Providing strategic and operational support to chambers of commerce, business associations and institutional platforms, including secretariat management and advocacy campaigns."),
            ("Diplomatic Engagement & International Cooperation", "Advising on bilateral and multilateral engagement, diplomatic initiatives, international partnerships and cross-border institutional cooperation."),
            ("Investment Promotion & Economic Diplomacy", "Developing investment promotion strategies, international outreach programmes and public\u2013private initiatives to attract investment."),
            ("Nation Branding & Public Diplomacy", "Developing country positioning, nation-branding strategies, cultural diplomacy initiatives and international communications programmes."),
            ("Government Communications & Strategic Events", "Supporting public-sector communications, stakeholder consultations, diplomatic conferences, policy forums and institutional events."),
        ],
    },
]

# Expertise sectors shown on home + /our-expertise
EXPERTISE = [
    ("Automotive & Manufacturing", "Heavy industry remains a driving force of national economic growth. With skilled labour and attractive government promotion packages, Thailand is a favourable destination to build a regional manufacturing hub. Eligible investors enjoy privileges ranging from CIT and import-duty exemptions to land ownership, with green and electric vehicles a particular government priority."),
    ("Corporate Social Responsibility", "CSR can be far more than a one-off activity. We help companies design strategic CSR programmes that benefit communities while strengthening reputation, stakeholder relationships and long-term licence to operate."),
    ("Digital Entertainment & E-sports", "We help clients navigate digital distribution platforms, adapt to evolving trends, foster audience engagement, and drive growth and innovation in digital entertainment, including the dynamic world of e-sports."),
    ("Environmental, Social & Governance (ESG)", "Strong ESG reporting demonstrates your commitment to sustainability and ethical business practices and opens doors to new global opportunities. Our ESG advisory helps you navigate this evolving landscape, mitigate risk and showcase your positive impact."),
    ("FMCG & Agriculture", "Premium, luxury and customised products for urban lifestyles have seen steady growth. The government promotes value-added products and smart farming to strengthen the Thai agricultural industry and support rural development."),
    ("Healthcare", "Thailand's universal health coverage is studied globally. With over 1,000 hospitals and many JCI-certified private providers, the country attracts over a million medical tourists annually for world-class, affordable treatment under rigorous quality regulation."),
    ("Infrastructure & Public Utilities", "Infrastructure and public utilities are fundamental to Thailand 4.0. Highways, railways, sea ports, airports, power, water and connectivity projects regularly invite public-private partnerships and foreign investment."),
    ("Technology, Digital & Startups", "Innovation, digital technology and startups are rising stars of the economy. The government is laying digital-age infrastructure and subsidising advanced-technology investment, supporting the transformation of traditional businesses for the digital future."),
]

# Team members grouped by section
TEAM = {
    "intro": (
        "Our team, comprised of seasoned professionals, delivers unparalleled expertise across "
        "public affairs, business diplomacy, strategic communications, and digital marketing. We "
        "leverage deep regional insights and global perspectives to navigate complex markets and "
        "drive impactful results."
    ),
    "groups": [
        {
            "title": "Meet the strategic minds behind MCG",
            "members": [
                ("Gift Kiranee Tammapiban-udom", "Partner & Co-Founder", "A certified lawyer and partnership advisor and former legal officer in the Finance Minister's Fiscal Policy Office. Gift supports Thai and international clients to navigate government processes and has led regulatory changes to improve ease of doing business across F&B, automotive, biotech and agriculture."),
                ("Ben Raiwin Kiatkwankul", "Partner & Co-Founder", "Former political analyst at the EU Delegation in Thailand, Ben brings international perspective combined with local insights, helping businesses overcome a challenging socio-political landscape. He is experienced in intelligence gathering and political campaigns that drive positive policy change."),
                ("Aom Chaniporn Buamahakul", "Chief Financial Officer", "A management accounting and compliance expert experienced in financial administration, analysis, control and risk management. Formerly at Ernst & Young Thailand, she has led internal costing and pricing projects at a leading Thai healthcare institute."),
                ("Kung Sarawut Thiramanit", "Associate Consultant", "A political analyst with deep expertise in International Relations and Public Administration. Kung's analytical skills and passion for international affairs and political economics enable him to dissect complex geopolitical scenarios and navigate governmental systems."),
            ],
        },
        {
            "title": "Special Counsellors",
            "members": [
                ("Patnaree Bhakdikhanasedh", "Special Counsellor", "Expert in government relations and strategic communications with over 10 years overseeing CLMV and pan-regional government relations projects."),
                ("Haruna Shino", "Special Counsellor", "Management consultant with expertise in alliances, M&A, sales channel development, and new business development at the global level, with a focus on cutting-edge technology."),
                ("Jun Kobayashi", "Special Counsellor", "Management consultant with strengths in acquisitions and investments when taking on challenges in new areas, with a focus on private equity funds and healthcare companies."),
                ("Lauren Brush", "Special Counsellor", "A strategic communications expert with over 15 years' experience across the US and EMEA, including advising UAE and Saudi Arabian ministries and healthcare providers."),
            ],
        },
        {
            "title": "Enterprise Thailand's Special Advisors",
            "members": [
                ("Prasom Fangtong", "Special Advisor", "Former Minister Counsellor to Nigeria and former Director of the African Affairs Division, Ministry of Foreign Affairs."),
                ("Chirathep Senivongs Na Ayudhaya", "Special Advisor", "Former Executive Vice President \u2013 Corporate Strategy, Stock Exchange of Thailand, and former Spokesman, Bank of Thailand."),
                ("Nattakan Jiarakul", "Special Advisor", "Lawyer with over ten years of experience in M&A, corporate, finance, compliance, foreign direct investment, litigation and public policy."),
                ("Dr Krislert Samphantharak", "Special Advisor", "Professor of Economics at UC San Diego's School of Global Policy and Strategy and Executive Director of the Puey Ungphakorn Institute for Economic Research."),
            ],
        },
    ],
}

# News / featured insights
INSIGHTS = [
    {
        "slug": "after-bangkok-imf-world-bank-2026-outcomes",
        "date": "October 22, 2026",
        "title": "After Bangkok: What the 2026 IMF-World Bank Annual Meetings Actually Produced",
        "summary": (
            "A framework, a set of host-country reflections, a loan agreement and a ministerial "
            "conversation do not carry equivalent weight. What the 2026 Annual Meetings left "
            "behind, sorted by institutional force."
        ),
        "tags": ["Political Economy", "Policy & Regulation", "Thailand", "Southeast Asia"],
        "body": [
            "The 2026 IMF-World Bank Annual Meetings in Bangkok produced a range of outcomes that "
            "differ sharply in their institutional weight. Distinguishing between a non-binding "
            "framework, host-country reflections, a concrete loan agreement, and a ministerial "
            "conversation is essential to understanding what was actually achieved.",
            "In this briefing, MCG sorts the meeting's deliverables by institutional force, "
            "assessing which commitments are likely to shape policy and which are primarily "
            "signalling. We examine the implications for Thailand's reform agenda and for "
            "investors monitoring the country's economic trajectory.",
        ],
    },
    {
        "slug": "thailand-2026-political-will-reform",
        "date": "October 18, 2026",
        "title": "Thailand 2026: Does It Really Lack Political Will?",
        "summary": (
            "As the IMF-World Bank meetings closed in Bangkok, the IMF's Managing Director observed "
            "that resilience does not fall from the sky. What Thailand's own reform record says "
            "about the distance between political intent and implementation."
        ),
        "tags": ["Political Economy", "Policy & Regulation", "Thailand", "Southeast Asia"],
        "body": [
            "\u201cResilience does not fall from the sky.\u201d The IMF Managing Director's remark at "
            "the close of the Bangkok meetings framed a familiar debate about Thailand: does the "
            "country lack the political will to reform?",
            "Drawing on Thailand's own reform record, this briefing examines the distance between "
            "political intent and implementation, and what it means for the country's medium-term "
            "economic prospects and its attractiveness to investors.",
        ],
    },
]

# Case studies (representative examples based on the firm's stated work)
CASE_STUDIES = [
    ("Market Entry for a Global Manufacturer", "Automotive & Manufacturing", "Advised a multinational manufacturer on BOI promotion, regulatory approvals and stakeholder engagement to establish a regional production hub in Thailand."),
    ("Regulatory Strategy in Healthcare", "Healthcare", "Developed a policy engagement and regulatory affairs strategy enabling a medical technology firm to navigate product registration and market access."),
    ("Policy Advocacy for a Digital Platform", "Technology & Startups", "Led an evidence-based advocacy campaign and stakeholder coalition to shape a favourable regulatory framework for a digital services provider."),
    ("Nation Branding & Economic Diplomacy", "Public Sector", "Supported a government entity with country positioning, international outreach and investment promotion around key economic priorities."),
    ("Crisis Communications & Reputation", "Strategic Communications", "Managed a sensitive public issue for a corporate client, coordinating media and stakeholder responses to protect reputation."),
    ("Cross-Border Investment Facilitation", "Business Diplomacy", "Facilitated a strategic partnership and foreign investment through embassy engagement, due diligence and business matching."),
]

PARTNERS = [
    "MCG Arabia / Maxwell Stamp KSA",
    "GP Consulting",
    "Enterprise Thailand",
    "Maverick Digital Solutions (MDS)",
]
