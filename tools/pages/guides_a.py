"""Guide bodies, part A: start here, local, skills."""

G = {}

G["contact-your-representatives"] = dict(
    cat="Skills", title="How to contact the people who represent you",
    lede="A short, specific message from someone who lives in the district gets read. Here is how to pick the right office and what to put in the message.",
    body="""
  <h2>Start with the right level of government</h2>
  <p>The fastest way to get nowhere is to ask the wrong office. As a rough guide:</p>
  <ul>
    <li><strong>City:</strong> zoning and building permits inside city limits, city streets and sidewalks, city police, parks, water and sewer.</li>
    <li><strong>County:</strong> elections, property assessments, the sheriff and jail, the courthouse, and land use outside city limits. Driver's licenses come from the county sheriff's office and vehicle registration from the county assessor, under state rules.</li>
    <li><strong>Highway district:</strong> in many parts of Idaho, a separate elected highway district looks after local roads. In Ada County, the Ada County Highway District runs nearly every local street, inside cities and out.</li>
    <li><strong>State:</strong> school funding, state highways, prisons, Medicaid, state parks, and state law in general.</li>
    <li><strong>Federal:</strong> Social Security and Medicare, veterans' benefits, immigration, passports, federal taxes, and the national forests and other federal land that cover much of Idaho.</li>
  </ul>
  <p>Not sure who yours are? Use <a href="../reps.html">Who represents you</a>.</p>

  <h2>What to put in the message</h2>
  <ol>
    <li><strong>Say you're a constituent.</strong> Give your city or town. Offices sort mail by whether you live in the district.</li>
    <li><strong>Make one ask.</strong> "Please vote yes on House Bill 123" is better than a general opinion. Include the bill or agenda item number if there is one.</li>
    <li><strong>Give your reason in a few sentences.</strong> How it affects you, your family or your work.</li>
    <li><strong>Keep it to a short page.</strong></li>
    <li><strong>Ask for a reply</strong> and include how to reach you.</li>
  </ol>

  <h2>Email, phone or in person</h2>
  <ul>
    <li><strong>Email</strong> is the easiest to send and the easiest to track. Every legislator's address is on the Legislature's website.</li>
    <li><strong>A phone call</strong> is quick. Idaho legislators are part-time and most share staff, so during the session the Legislative Information Center is the front door: 208-332-1000, or 800-626-0471 toll free. Have your one ask ready.</li>
    <li><strong>Out of session,</strong> legislators are home in their districts. Many list a home or cell number and hold town halls. This is often the best time to be heard.</li>
    <li><strong>In person</strong> works best at the local level. See <a href="speak-at-a-public-meeting.html">how to speak at a local public meeting</a>.</li>
  </ul>

  <h2>When you need help, not a vote</h2>
  <p>If you're stuck with a government agency, elected officials' offices can often help. Members of Congress have staff who handle problems with federal agencies. State legislators can ask a state agency about your case, and the Governor's office takes constituent requests too. Call the office and ask for help with a constituent issue.</p>
""",
    sources=[("https://legislature.idaho.gov/legislators/whosmylegislator/", "Who's My Legislator (Idaho Legislature)"),
             ("https://legislature.idaho.gov/resources/committeetestimony/", "Testifying before legislative committees, with Legislative Information Center contacts (Idaho Legislature)"),
             ("https://legislature.idaho.gov/legislators/congressional-delegation/", "Idaho's congressional delegation (Idaho Legislature)")])

G["local-government"] = dict(
    cat="Local", title="How local government works",
    lede="Most of the government you deal with day to day is local. In Idaho that means your county, your city if you live in one, your school district, and a handful of special districts you may not know you're in.",
    body="""
  <h2>Counties</h2>
  <p>Idaho has 44 counties. Each one is run by a board of three county commissioners, who act as both the county's lawmakers and its managers. Commissioners are elected by the whole county but each must live in a different commissioner district.</p>
  <p>Voters also elect six other county officers, each of whom runs their own office:</p>
  <ul>
    <li><strong>Clerk:</strong> runs elections, keeps the commissioners' records and the court's files, and records deeds.</li>
    <li><strong>Assessor:</strong> sets property values for tax purposes and handles vehicle registration.</li>
    <li><strong>Treasurer:</strong> collects property taxes.</li>
    <li><strong>Sheriff:</strong> law enforcement outside cities, the county jail, and driver's licenses.</li>
    <li><strong>Prosecuting attorney:</strong> prosecutes crimes and is the county's lawyer.</li>
    <li><strong>Coroner:</strong> investigates deaths.</li>
  </ul>
  <p>If you live outside city limits, the county is your local government for planning, zoning and building permits.</p>

  <h2>Cities</h2>
  <p>Idaho has about 200 incorporated cities, from Boise to towns of a few dozen people. Nearly all use the mayor-council form: voters elect a mayor, who runs the city day to day, and a council of four or six members, who pass ordinances and the budget. A few cities use the council-manager form, where the council hires a professional manager. City elections are nonpartisan and held in November of odd-numbered years.</p>

  <h2>School districts</h2>
  <p>Each school district is its own government, run by an elected board of trustees who hire the superintendent, set policy and adopt the budget. Trustees are unpaid and elected in November of odd-numbered years. Public charter schools have their own appointed boards.</p>

  <h2>Special districts</h2>
  <p>Idaho relies heavily on single-purpose districts, each with its own board, budget and, often, its own line on your property tax bill. Common ones:</p>
  <ul>
    <li><strong>Highway districts,</strong> which build and maintain local roads in much of the state.</li>
    <li><strong>Fire protection districts</strong> and ambulance districts.</li>
    <li><strong>Library districts.</strong></li>
    <li><strong>Irrigation and canal districts,</strong> which deliver water.</li>
    <li><strong>Cemetery, recreation, sewer and water districts.</strong></li>
    <li><strong>Public health districts.</strong> Idaho's seven health districts each serve several counties and are governed by boards the county commissioners appoint.</li>
    <li><strong>Urban renewal agencies,</strong> created by cities or counties to pay for redevelopment in a set area.</li>
  </ul>
  <p>Your property tax bill lists every district that taxes you. It is the quickest way to learn which ones you live in.</p>

  <section class="near-you" data-show="site,schools,districts" data-title="Your local governments" aria-label="Your local governments"></section>

  <h2>Where you can step in</h2>
  <ul>
    <li><strong>Meetings.</strong> Every one of these boards meets in public and must post its agenda ahead of time. See <a href="speak-at-a-public-meeting.html">how to speak at a local public meeting</a>.</li>
    <li><strong>Budget hearings.</strong> Each county, city and district must hold a public hearing on its budget before adopting it, usually in late summer. It is the one meeting a year where every program is on the table.</li>
    <li><strong>Elections.</strong> Small districts are often decided by a few dozen votes, and seats sometimes go unfilled for lack of candidates. See <a href="running-for-office.html">running for office</a>.</li>
    <li><strong>Appointed boards.</strong> Planning and zoning commissions, library boards and others are filled by appointment. See <a href="boards-and-commissions.html">serve on a board or commission</a>.</li>
  </ul>
""",
    sources=[("https://archive.sos.idaho.gov/blue_book/blue_book_2025-2026.pdf", "The Blue Book of Idaho, 2025-2026, county government section (Idaho Secretary of State)"),
             ("https://idcounties.org/wp-content/uploads/2025/10/Introduction-to-State-Local-Government.pdf", "Introduction to state and local government (Idaho Association of Counties)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/", "Idaho Statutes: Title 31 (counties), Title 50 (cities), Title 33 (schools), Title 40 (highways) (Idaho Legislature)")])

G["speak-at-a-public-meeting"] = dict(
    cat="Local", title="How to speak at a local public meeting",
    lede="City councils, county commissioners, school boards and highway districts make most of the decisions you feel day to day. Here is what Idaho law gives you, what it doesn't, and how to use two minutes well.",
    body="""
  <h2>What Idaho law gives you</h2>
  <p>Idaho's Open Meetings Law (Idaho Code Title 74, Chapter 2) covers the governing bodies of counties, cities, school districts, special districts and state boards and commissions.</p>
  <ul>
    <li><strong>You can attend.</strong> Meetings of a governing body are open to the public, and decisions must be made in the open (Idaho Code 74-203).</li>
    <li><strong>You get notice.</strong> A regular meeting needs at least five calendar days' notice and an agenda posted at least 48 hours ahead. A special meeting needs 24 hours' notice of both. A board that meets on a set schedule can post that schedule once a year, but each meeting still needs its 48-hour agenda (74-204).</li>
    <li><strong>The agenda has to be real.</strong> A board can generally decide only what is on the agenda, and items it will vote on must be marked as action items. Adding something late takes a vote and a stated reason it couldn't have been listed sooner.</li>
    <li><strong>Closed sessions are limited.</strong> A board can meet privately only for reasons the law lists, such as hiring, a specific employee's discipline, buying land or pending lawsuits. It takes a two-thirds roll call vote that names the reason, and no final decision can be made behind closed doors (74-206).</li>
    <li><strong>There are minutes.</strong> Written minutes must record who was there, every motion and every vote, and be available to the public (74-205).</li>
  </ul>

  <h2>What it doesn't give you</h2>
  <p><strong>The Open Meetings Law gives you the right to watch, not the right to speak.</strong> A board does not have to take public comment at an ordinary meeting. Most city councils and school boards choose to, under their own rules. Many county commissions take it less often.</p>
  <p><strong>Public hearings are different.</strong> When a law requires a hearing, the board must let people testify. That includes the yearly budget, most zoning and land use decisions, and many fee increases. If you want to be sure of being heard, a public hearing is the place.</p>

  <section class="near-you" data-show="meetings" data-title="Meetings near you" aria-label="Meetings near you"></section>

  <h2>Before the meeting</h2>
  <ol>
    <li><strong>Find the meeting.</strong> The <a href="../">calendar</a> lists what's coming up near you.</li>
    <li><strong>Read the agenda.</strong> Find the item you care about and note its number or title, and whether it is an action item or a public hearing.</li>
    <li><strong>Check how this body takes comment.</strong> Every body sets its own rules: whether you sign up ahead or at the door, how long you get, and whether you can speak by phone or video. Call the clerk if the website doesn't say.</li>
    <li><strong>If there's no comment period,</strong> email the members before the meeting, or ask the clerk how to get an item on a future agenda.</li>
  </ol>

  <h2>What to say</h2>
  <p>Time limits are short, often two or three minutes, so write it down and time yourself.</p>
  <ol>
    <li><strong>Who you are.</strong> Your name and that you live, work or own a business in the community. At a hearing you'll usually be asked for your address for the record.</li>
    <li><strong>What you're talking about.</strong> Name the agenda item.</li>
    <li><strong>What you want them to do.</strong> Vote yes, vote no, change something specific, or delay.</li>
    <li><strong>One reason.</strong> A short personal example lands better than a list of arguments.</li>
    <li><strong>Repeat the ask and thank them.</strong></li>
  </ol>

  <h2>After you speak</h2>
  <ul>
    <li><strong>Don't expect an answer on the spot.</strong> Most bodies listen during comment and don't respond.</li>
    <li><strong>Follow up in writing.</strong> Email the members the same points, plus anything you ran out of time for.</li>
    <li><strong>Watch for the vote.</strong> The decision may come at a later meeting.</li>
  </ul>

  <h2>If a board breaks the rules</h2>
  <p>A decision made at a meeting that broke the Open Meetings Law can be thrown out. Tell the board in writing first: it then has 14 days to respond and can fix the problem by redoing the decision in the open. Complaints about local boards go to the county prosecuting attorney, and complaints about state boards go to the Attorney General. A person affected by the decision can also go to court, but only within 30 days.</p>
""",
    sources=[("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH2/", "Idaho Code Title 74, Chapter 2, Open Meetings Law (Idaho Legislature)"),
             ("https://www.ag.idaho.gov/content/uploads/2026/07/OpenMeeting.pdf", "Idaho Open Meeting Law Manual, July 2026 (Idaho Attorney General)"),
             ("https://idcounties.org/wp-content/uploads/2025/10/Idaho-Open-Meeting-Law-2025.pdf", "Idaho Open Meeting Law, 2025 training summary (Idaho Association of Counties)")])

G["your-neighborhood"] = dict(
    cat="Local", title="What you can do in your neighborhood",
    lede="You don't need a title to change things on your block. Here are practical ways to get problems fixed and get people organized.",
    body="""
  <h2>Get a problem fixed</h2>
  <ul>
    <li><strong>Report it to the right place.</strong> Potholes, broken streetlights and missing signs go to whoever owns the road: the city, the county road department or the local highway district. In Ada County that is almost always the Ada County Highway District. Illegal dumping, weeds and junk vehicles go to city or county code enforcement.</li>
    <li><strong>Keep the reference number.</strong> If nothing happens, follow up with it. If nothing happens after that, contact your council member, county commissioner or highway district commissioner.</li>
    <li><strong>Bring neighbors.</strong> Five households reporting the same problem carries more weight than one.</li>
  </ul>

  <section class="near-you" data-show="site" data-title="Your city and county websites" aria-label="Your city and county websites"></section>

  <h2>Find out what's planned</h2>
  <ul>
    <li><strong>Watch for land use notices.</strong> Rezones, subdivisions and special use permits require a public hearing. Notice is published, mailed to nearby property owners and usually posted on the property about two weeks ahead. If you get one, the hearing date on it is your chance to testify.</li>
    <li><strong>Ask for records.</strong> Under Idaho's Public Records Act, anyone can ask a state or local agency for its records. If you are an Idaho resident, the agency must grant or deny the request within three working days, or tell you it needs up to ten, and the first two hours of staff time and the first 100 pages are free. Since a 2025 change to the law, people who don't live in Idaho wait up to 21 days, extendable to 35, and get no free hours or pages. See <a href="public-records-requests.html">how to request public records</a>.</li>
    <li><strong>Read the comprehensive plan.</strong> Every city and county has one, with a map of what kind of growth is planned where. Zoning decisions are supposed to follow it, so it is the best argument you can bring to a hearing.</li>
    <li><strong>Check the road plans.</strong> Highway districts and the Idaho Transportation Department publish multi-year project lists. Getting a project onto the list is easier than adding it later.</li>
  </ul>

  <h2>Get organized</h2>
  <ul>
    <li><strong>Join or start a neighborhood association.</strong> Some cities formally register neighborhood associations and notify them of nearby projects.</li>
    <li><strong>Hold a block party or cleanup.</strong> Cities often have simple permits for closing a residential street, and some lend cleanup supplies.</li>
    <li><strong>Make a phone tree or group chat.</strong> It sounds small, but it is what lets a neighborhood show up quickly when a decision is coming.</li>
  </ul>

  <h2>Take it to a meeting</h2>
  <p>When a problem needs a decision, not just a repair, bring it to your city council, county commissioners or highway district. See <a href="speak-at-a-public-meeting.html">how to speak at a local public meeting</a> and <a href="problem-to-policy.html">turning a personal problem into a policy ask</a>.</p>
""",
    sources=[("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH1/SECT74-103/", "Idaho Code 74-103, response to a public records request (Idaho Legislature)"),
             ("https://www.ag.idaho.gov/content/uploads/2026/07/PublicRecordsLaw.pdf", "Idaho Public Records Law Manual, July 2026 (Idaho Attorney General)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH2/", "Idaho Code Title 74, Chapter 2, Open Meetings Law (Idaho Legislature)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/", "Idaho Statutes: Title 67, Chapter 65, Local Land Use Planning (Idaho Legislature)")])

G["local-ballot-measures"] = dict(
    cat="Local", title="Local ballot measures",
    lede="Bonds, levies and local initiatives put taxing and spending decisions directly in front of voters. Idaho sets some of the highest bars in the country for passing them.",
    body="""
  <h2>Bonds: borrowing for big projects</h2>
  <p>A bond lets a school district, city, county or other district borrow money for something large, like a school or a fire station, and repay it with property taxes over many years.</p>
  <ul>
    <li><strong>Most bonds need a two-thirds yes vote.</strong> This comes from the Idaho Constitution. A school bond can get 60 percent and still fail.</li>
    <li><strong>A few need only a simple majority,</strong> including bonds for water and sewer systems.</li>
  </ul>

  <h2>Levies: property taxes for a set time</h2>
  <ul>
    <li><strong>Supplemental levies</strong> pay for school operations, such as staff, programs and buses, usually for one or two years. They pass with a simple majority.</li>
    <li><strong>Plant facilities levies</strong> pay for school buildings and repairs over several years without borrowing. They need at least 55 percent, and more for larger levies.</li>
    <li><strong>Other districts,</strong> such as fire and library districts, can ask voters to raise their levies too. The share of yes votes needed depends on the kind of levy and how long it lasts, so check the ballot language.</li>
  </ul>

  <h2>When they're on the ballot</h2>
  <ul>
    <li><strong>School measures</strong> can appear only in May or November. The Legislature removed the March and August election dates.</li>
    <li><strong>City and county bonds and levies</strong> go on the third Tuesday in May or the November election day.</li>
    <li><strong>City initiatives and referendums</strong> are voted on only at the November election in odd-numbered years (Idaho Code 34-1801B).</li>
  </ul>

  <h2>Local initiatives and referendums</h2>
  <p>Voters in Idaho cities and counties can propose an ordinance, or force a vote on one the council or commissioners just passed.</p>
  <ul>
    <li><strong>Signatures:</strong> 20 percent of the number of people who voted in the last general city election (for a city) or the last general county election (for a county).</li>
    <li><strong>Referendum deadline:</strong> for a city, within 60 days after the ordinance is published (Idaho Code 34-1801B). Ask the county clerk for a county's deadline.</li>
    <li><strong>Limits:</strong> local initiatives can't be used for zoning decisions.</li>
    <li><strong>Passing:</strong> a simple majority.</li>
  </ul>

  <h2>Before you vote</h2>
  <ul>
    <li><strong>Read the ballot language.</strong> It must state the purpose, the amount and the estimated cost per $100,000 of taxable value.</li>
    <li><strong>Check whether it replaces something.</strong> A levy that "renews" an expiring one may not raise your bill. A new one will.</li>
    <li><strong>Find your sample ballot</strong> through your county clerk or VoteIdaho.gov.</li>
    <li><strong>Go to the hearing.</strong> The board has to vote in a public meeting to put a measure on the ballot, well before the election.</li>
    <li><strong>Check who can vote and sign.</strong> To vote or sign a petition in Idaho, you must be a U.S. citizen, at least 18, living in Idaho and your county for at least 30 days, and registered to vote (Idaho Code 34-402). Permanent residents (green card holders) and other noncitizens can't vote or sign petitions, even in local elections.</li>
  </ul>
""",
    sources=[("https://legislature.idaho.gov/statutesrules/idstat/Title34/T34CH18/SECT34-1801B/", "Idaho Code 34-1801B, city initiatives and referendums (Idaho Legislature)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/title34/t34ch4/sect34-402", "Idaho Code 34-402, who can vote (Idaho Legislature)"),
             ("https://ballotpedia.org/Laws_governing_local_ballot_measures_in_Idaho", "Laws governing local ballot measures in Idaho (Ballotpedia)"),
             ("https://ballotpedia.org/School_bond_and_tax_elections_in_Idaho", "School bond and tax elections in Idaho (Ballotpedia)"),
             ("https://www.idahoednews.org/top-news/emerging-outliers-school-facility-measures-grow-harder-to-pass/", "School facility measures and their approval thresholds (Idaho Education News, June 2026)"),
             ("https://voteidaho.gov/county-clerk/", "County elections offices (Idaho Secretary of State)")])

G["two-minute-pitch"] = dict(
    cat="Skills", title="Build a two-minute pitch for your cause",
    lede="Public comment, a hallway conversation with a legislator, a meeting with a commissioner: most chances to make your case last about two minutes. Here is how to use them.",
    body="""
  <h2>The shape of a good pitch</h2>
  <ol>
    <li><strong>Who you are (10 seconds).</strong> Your name, where you live, and why you have a stake: "I'm a parent in Nampa," "I run a small business in Sandpoint."</li>
    <li><strong>The problem (30 seconds).</strong> One clear sentence about what's wrong, then a short, specific example. A real story beats a statistic, and a story with one number beats both.</li>
    <li><strong>The fix (30 seconds).</strong> What you want done, as concretely as you can: a bill number, a budget line, an agenda item, a change to a policy.</li>
    <li><strong>Why it's worth it (30 seconds).</strong> Who benefits, what it costs or saves, and who else supports it.</li>
    <li><strong>The ask (10 seconds).</strong> Say exactly what you want this person to do: vote yes, co-sponsor, meet with you, add it to an agenda.</li>
  </ol>

  <h2>Make it land</h2>
  <ul>
    <li><strong>Know your audience.</strong> What does this person care about? What have they said or voted on before? Connect your issue to that.</li>
    <li><strong>One ask, not five.</strong> Pick the one thing that matters most right now.</li>
    <li><strong>Practice out loud and time it.</strong> Two minutes is about 250 spoken words. Legislative committee chairs often hold testimony to two or three minutes and will cut you off.</li>
    <li><strong>Leave something behind.</strong> A one-page summary with your contact information.</li>
    <li><strong>Follow up.</strong> Send a thank-you within a day, and repeat your ask.</li>
  </ul>

  <h2>Telling your own story</h2>
  <p>If you're speaking from personal experience, share only what you're comfortable having on the public record. Meetings are often recorded and posted online, and the Legislature's committee hearings are streamed live.</p>
""",
    sources=[("https://legislature.idaho.gov/resources/committeetestimony/", "Testifying before legislative committees (Idaho Legislature)")])

G["read-a-bill-or-agenda"] = dict(
    cat="Skills", title="How to read a bill or an agenda",
    lede="Bills and agendas look dense, but they follow patterns. Once you know the patterns you can find what matters in a few minutes.",
    body="""
  <h2>Reading an Idaho bill number</h2>
  <ul>
    <li><strong>H 123</strong> is a House bill. <strong>S 1045</strong> is a Senate bill. Senate bills start at 1001, so a four-digit number means it began in the Senate.</li>
    <li><strong>A lowercase "a" means amended.</strong> H 123a has been amended once and H 123aa twice. "aaS" means one of those amendments was made in the Senate.</li>
    <li><strong>HJR and SJR</strong> are joint resolutions, used to propose amendments to the Idaho Constitution. These go to voters.</li>
    <li><strong>HCR and SCR</strong> are concurrent resolutions, used for the Legislature's own business and to approve or reject agency rules.</li>
    <li><strong>HJM and SJM</strong> are joint memorials: formal messages to Congress or the President. They don't change Idaho law.</li>
    <li><strong>RS</strong> followed by a number is a draft that hasn't been introduced yet. It becomes a bill when a committee votes to print it.</li>
  </ul>

  <h2>Reading the bill itself</h2>
  <ol>
    <li><strong>Start with the Statement of Purpose.</strong> Every Idaho bill comes with a one-page statement of what it does and a fiscal note estimating what it costs. Both are written by the sponsor, so read them as the sponsor's case, not a neutral analysis.</li>
    <li><strong>Read the title.</strong> The long sentence at the top lists every section of law the bill touches.</li>
    <li><strong>Look for the markup.</strong> <u>Underlined</u> text is being added to the law. <s>Struck-through</s> text is being removed. Plain text is current law that stays.</li>
    <li><strong>Check the last section.</strong> It says when the law takes effect. Most take effect July 1. An "emergency clause" makes it take effect as soon as the Governor signs.</li>
    <li><strong>Check the bill's page</strong> on the Legislature's website for its history: where it is now and how each member voted.</li>
  </ol>

  <h2>Reading a local agenda</h2>
  <ul>
    <li><strong>Action items.</strong> Idaho law requires anything the board will vote on to be marked as an action item. If your issue isn't marked, no decision is coming at this meeting.</li>
    <li><strong>Consent agenda.</strong> Routine items passed in one vote with no discussion. A board member can pull an item off for discussion, and you can ask one to.</li>
    <li><strong>Public hearings.</strong> Items where the law requires the board to take testimony. Each lists what is being decided.</li>
    <li><strong>Executive session.</strong> A closed-door portion. The agenda must cite the section of Idaho Code that allows it, and no final decision can be made there.</li>
    <li><strong>The packet.</strong> The staff reports, maps and draft ordinances behind each item. It is usually a separate, much longer file, and it is where the details are.</li>
  </ul>

  <h2>Shortcuts</h2>
  <ul>
    <li><strong>Search the file</strong> for your street, your school or the key word.</li>
    <li><strong>Read the staff recommendation first.</strong> Boards follow it most of the time.</li>
    <li><strong>Ask the clerk or the committee secretary</strong> when something is unclear. Answering that kind of question is part of their job.</li>
  </ul>
""",
    sources=[("https://legislature.idaho.gov/resources/howabillbecomesalaw/", "How a bill becomes a law (Idaho Legislature)"),
             ("https://legislature.idaho.gov/", "Bill text, statements of purpose and bill history (Idaho Legislature)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH2/", "Idaho Code Title 74, Chapter 2, Open Meetings Law (Idaho Legislature)")])

G["media-literacy"] = dict(
    cat="Skills", title="Media literacy: sorting good information from bad",
    lede="Before you share, argue or show up at a meeting, it's worth knowing whether what you read is true. These habits take a minute and catch most problems.",
    body="""
  <h2>Before you believe it</h2>
  <ul>
    <li><strong>Check the source.</strong> Who published this? Do they have a track record, and do they correct mistakes? An unfamiliar site that looks like a news outlet might not be one.</li>
    <li><strong>Read past the headline.</strong> Headlines are written to get clicks and often overstate what the story says.</li>
    <li><strong>Look for the original.</strong> If a post cites a study, a law or a quote, find the original. Bills, agendas, budgets and court records are usually public.</li>
    <li><strong>Check the date.</strong> Old stories get reshared as if they were new.</li>
    <li><strong>See who else is reporting it.</strong> If a big claim appears in only one place, wait.</li>
  </ul>

  <h2>Watch for these</h2>
  <ul>
    <li><strong>Strong emotion.</strong> Content built to make you angry or afraid spreads fastest. That's a cue to slow down.</li>
    <li><strong>Edited or fake images and video,</strong> including AI-generated ones. Look for odd details, and search for the image to see where it first appeared.</li>
    <li><strong>Missing context.</strong> A real clip or number can mislead when it's cut short.</li>
    <li><strong>Bill summaries from advocates.</strong> Groups on every side score and summarize Idaho bills. Read the bill's own text before you trust anyone's description of it.</li>
  </ul>

  <h2>Local news matters</h2>
  <p>Local reporters cover city councils, school boards and county decisions that national outlets never will. Many Idaho towns have lost their daily paper. Supporting the local news you still have, and reading it, is one of the easiest ways to stay informed about decisions close to home.</p>

  <h2>Go to the source on government</h2>
  <p>For local and state decisions, the primary sources are usually online: meeting agendas and recordings, the Legislature's bill pages and live video, and agency reports. The <a href="../">calendar</a> links to each meeting's official page. For elections, your county clerk and VoteIdaho.gov are the official word on dates, polling places and results.</p>
""",
    sources=[("https://www.newslit.org/", "News Literacy Project"),
             ("https://voteidaho.gov/", "VoteIdaho.gov (Idaho Secretary of State)"),
             ("https://www.idahoptv.org/shows/idahoinsession/Legislature/", "Idaho in Session, live video of the Legislature (Idaho Public Television)")])

G["volunteer-and-public-service"] = dict(
    cat="Everyday", title="Volunteering and public service jobs",
    lede="Showing up at meetings is one way to take part. Giving your time, or making public service your work, is another.",
    body="""
  <h2>Volunteer</h2>
  <ul>
    <li><strong>Serve Idaho</strong> is the Governor's commission on service and volunteerism. It runs AmeriCorps programs in Idaho and points people toward volunteer opportunities around the state.</li>
    <li><strong>Work the polls.</strong> County clerks hire poll workers for every election. It is paid, it takes one long day, and clerks are almost always short of people. Poll workers must be U.S. citizens, at least 16, and able to read and write English, according to the Secretary of State. Contact your county elections office.</li>
    <li><strong>Your library, school and parks.</strong> Most take volunteers directly. Friends of the Library groups and parent organizations are easy places to start.</li>
    <li><strong>Search and rescue, fire and ambulance.</strong> Much of rural Idaho depends on volunteer responders, usually organized through the sheriff's office or the local fire district.</li>
    <li><strong>State parks and Fish and Game</strong> both run volunteer programs, from campground hosts to habitat projects.</li>
  </ul>

  <h2>Serve on a board</h2>
  <p>Planning commissions, library boards and state advisory councils are filled by residents. See <a href="boards-and-commissions.html">serve on a board or commission</a>.</p>

  <h2>Work in government</h2>
  <ul>
    <li><strong>State jobs.</strong> The Idaho Division of Human Resources lists openings across state agencies and explains how hiring works.</li>
    <li><strong>City, county and school district jobs</strong> are posted on each government's own website.</li>
    <li><strong>IdahoWorks,</strong> run by the Idaho Department of Labor, lists public and private jobs statewide.</li>
    <li><strong>Federal jobs</strong> in Idaho, including with the Forest Service, the Bureau of Land Management and the Idaho National Laboratory's federal offices, are posted on USAJOBS.</li>
    <li><strong>The Legislature</strong> hires session staff each winter, including committee secretaries and pages. High school seniors can apply to be pages.</li>
  </ul>

  <h2>Run for something</h2>
  <p>Many local seats go uncontested. See <a href="running-for-office.html">running for office</a>.</p>
""",
    sources=[("https://serve.idaho.gov/", "Serve Idaho, the Governor's Commission on Service and Volunteerism"),
             ("https://dhr.idaho.gov/information-about-state-careers/", "Information about state careers (Idaho Division of Human Resources)"),
             ("https://idahoworks.gov/", "IdahoWorks (Idaho Department of Labor)"),
             ("https://voteidaho.gov/poll-workers/", "Become an election worker (Idaho Secretary of State)"),
             ("https://voteidaho.gov/county-clerk/", "County elections offices (Idaho Secretary of State)"),
             ("https://www.usajobs.gov/", "USAJOBS")])

G["problem-to-policy"] = dict(
    cat="Problem solving", title="Turning a personal problem into a policy ask",
    lede="Plenty of laws started with one person's bad experience. Here is how to tell whether your problem has a government fix, and how to ask for it.",
    body="""
  <h2>Is it a personal problem or a government one?</h2>
  <p>Ask yourself three questions:</p>
  <ul>
    <li><strong>Is it happening to other people too?</strong> If neighbors, coworkers or people online describe the same thing, it may be a pattern, not bad luck.</li>
    <li><strong>Does a rule cause it, or fail to prevent it?</strong> A fee, a deadline, a missing service, a law that doesn't fit how people live.</li>
    <li><strong>Is a government body responsible for that rule?</strong> If yes, you have someone to ask.</li>
  </ul>

  <h2>Find the right level</h2>
  <ul>
    <li><strong>Start with the agency that runs the program.</strong> Many problems are about how a rule is carried out, not the rule itself, and the agency can fix them.</li>
    <li><strong>If the rule itself is the problem,</strong> find who wrote it: a city council, county commissioners, a district board, the Legislature, a state agency's rules, or Congress. See <a href="contact-your-representatives.html">how to contact the people who represent you</a>.</li>
    <li><strong>Agency rules get a second look.</strong> In Idaho, state agency rules have to go before the Legislature, which can reject them. If your problem is a rule, the agency's rulemaking comment period and the legislative committee that reviews it are both places to speak up.</li>
  </ul>

  <h2>Shape the ask</h2>
  <ol>
    <li><strong>Describe the problem in one sentence.</strong></li>
    <li><strong>Show it isn't just you.</strong> Collect a few other stories, and any numbers you can find.</li>
    <li><strong>Propose a specific change.</strong> "Let people renew online," "extend the deadline to 30 days," "add a waiver for people who can't pay." You don't need perfect legal language.</li>
    <li><strong>Find allies.</strong> Nonprofits, business groups, churches or neighborhood associations may already be working on it.</li>
    <li><strong>Find a champion.</strong> One elected official who will carry the idea is worth more than ten who agree in passing. In the Legislature, a bill needs a sponsor and a committee chair willing to give it a hearing.</li>
  </ol>

  <h2>Mind the calendar</h2>
  <p>Idaho's Legislature meets for about three months starting in January, and bills that don't pass die when it adjourns. The time to bring a legislator an idea is summer and fall, when they're home and drafting. By February it is usually too late for that year.</p>

  <h2>Be ready for a long road</h2>
  <p>Most changes take more than one try. Bills often take several sessions to pass, and local changes may wait for the next budget. Keep a record of each conversation, keep your allies informed, and come back.</p>
  <p>When you're ready to make your case in person, use <a href="two-minute-pitch.html">build a two-minute pitch</a>.</p>
""",
    sources=[("https://legislature.idaho.gov/resources/howabillbecomesalaw/", "How a bill becomes a law (Idaho Legislature)"),
             ("https://legislature.idaho.gov/resources/committeetestimony/", "Testifying before legislative committees (Idaho Legislature)")])
