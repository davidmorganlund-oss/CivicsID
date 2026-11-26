"""Guide bodies, part B: state and federal."""

G = {}

G["legislature"] = dict(
    cat="State", title="How the Idaho Legislature works",
    lede="A hundred and five part-time legislators write Idaho's laws and its budget in about three months each winter. Here is who they are, how the session runs, and where your voice counts.",
    body="""
  <h2>Who's in it</h2>
  <ul>
    <li><strong>35 districts.</strong> Each elects one senator and two representatives, in House seats A and B. That makes 35 senators and 70 representatives. All three of yours represent the same district.</li>
    <li><strong>Two-year terms for everyone.</strong> Every seat in both chambers is on the ballot in every even-numbered year. There are no term limits.</li>
    <li><strong>New terms start December 1</strong> after the November election. Members meet briefly in early December to organize and pick leaders.</li>
    <li><strong>It's a part-time job.</strong> Most legislators have other work and are home in their districts from spring to December.</li>
    <li><strong>District lines</strong> are redrawn after each census by a bipartisan citizen commission, not by the Legislature.</li>
  </ul>
  <p>Find yours with <a href="../reps.html">Who represents you</a>.</p>

  <h2>The session calendar</h2>
  <ul>
    <li><strong>It starts in early January.</strong> The session opens on the Monday closest to January 9. In 2027 that is January 11. The Governor gives the State of the State address and releases a budget proposal that day.</li>
    <li><strong>There's no fixed end date.</strong> The session runs until the work is done, usually around three months, ending in late March or April.</li>
    <li><strong>Everything dies at the end.</strong> A bill that hasn't passed when the Legislature adjourns is dead. It has to be introduced again the next year.</li>
    <li><strong>Between sessions,</strong> interim committees study specific issues and the budget committee meets a few times. Those meetings are on the <a href="../?cat=legislature">calendar</a>.</li>
  </ul>

  <h2>How a bill moves</h2>
  <ol class="steps">
    <li><strong>A draft, called an RS.</strong> A legislator has an idea drafted. Before it is a bill, a committee holds a short "print hearing" and votes on whether to introduce it. No public testimony is taken at this step.</li>
    <li><strong>Introduction.</strong> The bill gets a number, is read on the floor and is sent to a committee.</li>
    <li><strong>Committee hearing.</strong> The committee chair decides whether and when the bill gets a hearing. This is where the public testifies. The committee can send the bill to the floor with a "do pass" recommendation, send it to be amended, or hold it, which usually kills it.</li>
    <li><strong>Floor vote.</strong> The bill is read on three separate days. Debate and the vote happen at third reading. A majority of members present passes it.</li>
    <li><strong>The other chamber.</strong> It goes through the same steps there. If the second chamber amends it, the first has to agree.</li>
    <li><strong>The Governor.</strong> During the session the Governor has five days, not counting Sundays, to sign or veto. A bill left alone becomes law without a signature. After the Legislature adjourns the Governor has ten days. A veto can be overridden by two-thirds of the members present in each chamber.</li>
    <li><strong>It takes effect.</strong> Most new laws take effect July 1.</li>
  </ol>

  <h2>Deadlines inside the session</h2>
  <ul>
    <li><strong>Individual members can introduce bills only in the first few weeks:</strong> through the 12th day in the Senate and the 20th day in the House. After that, bills have to come from a committee, and after the 36th day in the House only from certain committees.</li>
    <li><strong>Leadership sets target dates</strong> each year for moving bills between chambers. They slip often.</li>
    <li><strong>The end of the session moves fast.</strong> Bills can be heard and passed with very little notice in the final weeks.</li>
  </ul>

  <h2>The budget committee</h2>
  <p>The Joint Finance-Appropriations Committee, known as JFAC, is ten senators and ten representatives who write every agency's budget. It is the most powerful committee in the building. See <a href="state-budgets.html">the state budget and how to influence it</a>.</p>

  <h2>Where your voice counts</h2>
  <ul>
    <li><strong>Before the session.</strong> Summer and fall are when legislators decide what to sponsor. They're home and reachable.</li>
    <li><strong>The committee chair.</strong> A bill that never gets a hearing never gets a vote. If you want a bill heard, or not heard, the chair is who decides.</li>
    <li><strong>The committee hearing.</strong> This is the only step with public testimony. See <a href="weigh-in-on-a-state-bill.html">how to weigh in on a state bill</a>.</li>
    <li><strong>Your own three legislators,</strong> before the floor vote.</li>
    <li><strong>The Governor's office,</strong> once a bill has passed both chambers.</li>
  </ul>
""",
    sources=[("https://legislature.idaho.gov/resources/howabillbecomesalaw/", "How a bill becomes a law (Idaho Legislature)"),
             ("https://legislature.idaho.gov/legislators/", "Legislators (Idaho Legislature)"),
             ("https://legislature.idaho.gov/committees/", "Committees (Idaho Legislature)"),
             ("https://legislature.idaho.gov/statutesrules/idconst/", "Idaho Constitution, Articles III and IV (Idaho Legislature)"),
             ("https://www.idahoptv.org/shows/idahoinsession/Legislature/", "Idaho in Session, live video of the Legislature (Idaho Public Television)")])

G["weigh-in-on-a-state-bill"] = dict(
    cat="State", title="How to weigh in on a state bill",
    lede="Idaho's session is short and its hearings are scheduled fast. Here are four ways to tell the Legislature what you think, and the timing that catches people out.",
    body="""
  <h2>1. Contact your own legislators</h2>
  <p>You have one senator and two representatives. A short email that names the bill and says you live in the district is the simplest thing you can do, and it works at any stage. Find them with <a href="../reps.html">Who represents you</a>. During the session you can also reach the Legislative Information Center at 208-332-1000 or 800-626-0471.</p>

  <h2>2. Testify at the committee hearing</h2>
  <p>The committee hearing is the one point where the public speaks.</p>
  <ol>
    <li><strong>Find the hearing.</strong> Each committee posts an agenda listing the bills it will hear. Agendas are on the Legislature's website and on the <a href="../?cat=legislature">calendar</a>.</li>
    <li><strong>Register.</strong> The agenda and the committee's web page link to a testimony registration form. You'll give your name, address, any group you represent, whether you're for or against, and whether you'll be there in person or remote.</li>
    <li><strong>Remote testimony depends on the committee.</strong> Most chairs allow testimony by video or phone, but not all, and not at every meeting. The registration form shows whether it is offered.</li>
    <li><strong>Expect two or three minutes.</strong> The chair sets the time limit and can cap the total testimony. Registering doesn't guarantee you'll be called.</li>
    <li><strong>Follow the room's rules.</strong> No applause, signs or demonstrations. The chair can ask people to leave.</li>
  </ol>

  <h2>3. Send written testimony</h2>
  <p>Email written testimony to the committee secretary, whose address is on the committee's page. The Legislature recommends sending it even if you plan to speak, in case time runs out or a remote connection fails. Keep it to a page and put the bill number and your position in the first line.</p>

  <h2>4. Write the committee chair and the Governor</h2>
  <ul>
    <li><strong>The chair</strong> decides whether a bill gets a hearing at all. If a bill you care about is sitting in committee, the chair is the person to ask.</li>
    <li><strong>The Governor</strong> has five days, not counting Sundays, to sign or veto a bill that reaches the desk during the session. The Governor's office takes messages by phone and web form.</li>
  </ul>

  <h2>Timing that catches people</h2>
  <ul>
    <li><strong>Hearings can be scheduled with very little notice,</strong> sometimes a day. Check the agenda daily when a bill you care about is in committee.</li>
    <li><strong>Agendas change.</strong> Bills get pulled or moved, and a hearing may not happen when it was first listed.</li>
    <li><strong>The first hearing isn't a hearing.</strong> When a draft is first introduced, the committee only votes on whether to print it. Testimony comes later, at the full hearing.</li>
    <li><strong>You get two chances.</strong> A bill that passes one chamber gets a new committee hearing in the other.</li>
    <li><strong>Nothing carries over.</strong> A bill that doesn't pass by the end of the session is dead and has to start again the next January.</li>
  </ul>

  <h2>Watch from anywhere</h2>
  <p>Idaho Public Television streams floor sessions and committee hearings live through Idaho in Session, and the Legislature's website archives the video. Each bill's page shows its text, its statement of purpose, where it stands and how members voted.</p>
""",
    sources=[("https://legislature.idaho.gov/resources/committeetestimony/", "Testifying before legislative committees (Idaho Legislature)"),
             ("https://legislature.idaho.gov/remote-testimony/", "Remote testimony (Idaho Legislature)"),
             ("https://legislature.idaho.gov/committees/senatecommittees/", "Senate committees, with secretaries' contacts (Idaho Legislature)"),
             ("https://legislature.idaho.gov/committees/housecommittees/", "House committees, with secretaries' contacts (Idaho Legislature)"),
             ("https://www.idahoptv.org/shows/idahoinsession/Legislature/", "Idaho in Session (Idaho Public Television)")])

G["state-budgets"] = dict(
    cat="State", title="The state budget and how to influence it",
    lede="Idaho doesn't pass one big budget bill. It passes a separate spending bill for each agency, all written by one committee. Here is the yearly cycle and when each part is open to you.",
    body="""
  <h2>The basics</h2>
  <ul>
    <li><strong>The fiscal year</strong> runs from July 1 to June 30. Fiscal year 2028 starts July 1, 2027.</li>
    <li><strong>It has to balance.</strong> The Idaho Constitution doesn't allow the state to spend more than it expects to take in.</li>
    <li><strong>Three kinds of money.</strong> The General Fund comes mostly from income and sales taxes and is what legislators argue over. Dedicated funds are fees and taxes tied to a purpose, like fuel taxes for roads. Federal funds come with federal rules.</li>
    <li><strong>Public schools are the biggest piece</strong> of the General Fund, followed by health and human services.</li>
  </ul>

  <h2>The yearly cycle</h2>
  <ol class="steps">
    <li><strong>Summer: agencies build their requests.</strong> Starting in July, each agency writes its request for the next fiscal year, following instructions from the Governor's budget office.</li>
    <li><strong>September 1: requests are due.</strong> Agencies send them to the Governor's Division of Financial Management and to the Legislature's budget staff. The requests are public.</li>
    <li><strong>Fall: the Governor decides.</strong> The Governor's staff review the requests and the Governor settles on a recommendation.</li>
    <li><strong>January: the Governor's budget.</strong> It is released on the first day of the session. The Legislative Budget Book puts each agency's request and the Governor's recommendation side by side.</li>
    <li><strong>January and February: JFAC.</strong> The Joint Finance-Appropriations Committee, ten senators and ten representatives, hears from each agency and then votes on each budget.</li>
    <li><strong>February and March: the bills.</strong> Each JFAC decision becomes an appropriation bill that has to pass the House and the Senate and be signed by the Governor. If one fails, JFAC writes a new one.</li>
    <li><strong>July 1: it takes effect.</strong></li>
  </ol>

  <h2>Where you can weigh in</h2>
  <ul>
    <li><strong>The agency, in spring and summer.</strong> The easiest time to get something into a budget is before the request is written. Many agencies answer to a board or commission that approves the request at a public meeting.</li>
    <li><strong>The Governor's office, in the fall.</strong></li>
    <li><strong>JFAC members, in December and January.</strong> JFAC's hearings are mostly for agencies to present, and public testimony is uncommon, so email is the practical route. Members from your part of the state are the ones to start with.</li>
    <li><strong>Your own legislators, before the floor votes.</strong> Every appropriation bill gets a vote in both chambers. See <a href="../reps.html">Who represents you</a>.</li>
  </ul>

  <h2>Local budgets work differently</h2>
  <p>Your city, county, school district and other local districts each adopt their own budget, and each must hold a public hearing on it first. Counties and most cities start their fiscal year October 1 and hold the hearing in August or early September. School districts start July 1 and hold theirs in June. That hearing is open to anyone, and it is where local property tax levels are set.</p>

  <h2>Following the money</h2>
  <p>The Legislature's budget office publishes the Legislative Budget Book before each session and a plain summary of what passed afterward. The State Controller's Transparent Idaho website shows state spending, payroll and local government budgets.</p>
""",
    sources=[("https://dfm.idaho.gov/citizens/budget-process/", "Budget process (Idaho Division of Financial Management)"),
             ("https://legislature.idaho.gov/lso/bpa/process/", "The budget process, with the statutes behind it (Idaho Legislative Services Office)"),
             ("https://legislature.idaho.gov/committees/joint-standing/", "Joint standing committees, including the Joint Finance-Appropriations Committee (Idaho Legislature)"),
             ("https://legislature.idaho.gov/statutesrules/idconst/", "Idaho Constitution, Article VII (Idaho Legislature)")])

G["boards-and-commissions"] = dict(
    cat="State", title="Serve on a board or commission",
    lede="Hundreds of decisions in Idaho, from zoning to professional licenses to fish and game seasons, are made or shaped by boards of ordinary residents. Most seats are filled by appointment, and many go begging.",
    body="""
  <h2>What these boards do</h2>
  <ul>
    <li><strong>Some decide.</strong> A planning and zoning commission rules on permits. The Fish and Game Commission sets seasons. Licensing boards discipline professionals.</li>
    <li><strong>Some advise.</strong> A parks board or an advisory council makes recommendations to the elected officials who decide.</li>
    <li><strong>Most are unpaid</strong> or pay a small amount per meeting, and meet once or twice a month.</li>
  </ul>

  <section class="near-you" data-show="boards" data-title="Boards near you" aria-label="Boards near you"></section>

  <h2>City and county boards</h2>
  <ul>
    <li><strong>Cities:</strong> the mayor usually appoints and the council confirms. Common boards are planning and zoning, parks, the library board, historic preservation, arts and the urban renewal agency.</li>
    <li><strong>Counties:</strong> the three commissioners appoint. Common boards are planning and zoning, the fair board, weed control, and the county's seats on regional boards like the public health district.</li>
    <li><strong>How to apply:</strong> most have a short application on the city or county website, or through the clerk. If you don't see openings listed, ask the clerk or the commissioners' office. Small counties often fill seats by word of mouth, and saying you're interested is enough to get on the list.</li>
  </ul>

  <h2>State boards, commissions and councils</h2>
  <p>The Governor appoints members to Idaho's state boards. Many appointments also need confirmation by the Senate.</p>
  <ol>
    <li><strong>Pick a board.</strong> The Governor's appointments page has the full list of boards, commissions and councils.</li>
    <li><strong>Check the vacancies.</strong> A separate page lists open seats and seats opening in the next 60 days. Many seats have requirements set in law, such as living in a certain region, belonging to a certain party or holding a certain license.</li>
    <li><strong>Fill out the application.</strong> It is a form on the appointments page. It has to be complete, signed and dated, with a resume attached.</li>
    <li><strong>Mail it</strong> to the Governor's office, attention Appointments. The address is on the form.</li>
    <li><strong>A recommendation helps.</strong> Someone else can recommend you through a form on the same page. A note from your legislator helps too.</li>
  </ol>
  <p>Questions go to the Governor's office at 208-334-2100.</p>

  <h2>Before you apply</h2>
  <ul>
    <li><strong>Go to a meeting first.</strong> You'll see what the board really does and how much reading it takes. The <a href="../">calendar</a> lists many of them.</li>
    <li><strong>Know the rules you'd be under.</strong> Board members are covered by Idaho's open meetings, public records and ethics laws. You can't decide matters you have a financial stake in.</li>
    <li><strong>You don't need to be an expert.</strong> Most boards want residents who show up, read the packet and ask good questions.</li>
  </ul>
""",
    sources=[("https://gov.idaho.gov/appointments/", "Appointments: the list of boards and the application (Office of the Governor)"),
             ("https://gov.idaho.gov/appointment-vacancies/", "Appointment vacancies (Office of the Governor)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH2/", "Idaho Code Title 74, Chapter 2, Open Meetings Law (Idaho Legislature)")])

G["campaign-finance"] = dict(
    cat="State", title="Following the money in Idaho politics",
    lede="Idaho's Sunshine Law makes candidates, political committees and lobbyists report where their money comes from and where it goes. All of it is searchable online.",
    body="""
  <h2>Who reports, and to whom</h2>
  <ul>
    <li><strong>One office for everything.</strong> Since 2020, campaign finance at every level in Idaho, from school board to Governor, is reported to the Secretary of State.</li>
    <li><strong>Candidates</strong> report every contribution and every expense, including their own money.</li>
    <li><strong>Political committees</strong> (PACs) and groups making independent expenditures report too.</li>
    <li><strong>Lobbyists</strong> register with the Secretary of State and report what they spend.</li>
    <li><strong>Candidates for Congress and President</strong> report to the Federal Election Commission instead.</li>
  </ul>

  <h2>Where to look</h2>
  <ul>
    <li><strong>The Sunshine Portal</strong> has reports from 2023 on: search by candidate, committee or donor.</li>
    <li><strong>The older Sunshine site</strong> has 2020 through 2023, including local candidates from those years.</li>
    <li><strong>A data archive</strong> covers 2000 through 2019 for state races. Local records from before 2020 are with the county or city clerk.</li>
    <li><strong>FEC.gov</strong> has federal candidates.</li>
  </ul>

  <h2>The limits</h2>
  <p>A person, business or political committee can give a candidate, per election:</p>
  <ul>
    <li><strong>$5,000</strong> for a statewide office such as Governor.</li>
    <li><strong>$1,000</strong> for the Legislature or a judicial office.</li>
  </ul>
  <p>The primary and the general election count separately. The Legislature considered raising these limits in 2026, so check the Secretary of State's current guides before you rely on a number.</p>

  <h2>When reports come out</h2>
  <ul>
    <li><strong>Monthly in an election year,</strong> due on the 10th.</li>
    <li><strong>Once a year otherwise,</strong> due January 10.</li>
    <li><strong>Within 48 hours</strong> for any single contribution of $1,000 or more.</li>
  </ul>

  <h2>What to look for</h2>
  <ul>
    <li><strong>Who gives the most,</strong> and whether they're in the district.</li>
    <li><strong>Money from committees.</strong> Look up the committee itself to see who funds it.</li>
    <li><strong>Independent spending.</strong> Groups can spend to support or oppose a candidate without giving to the campaign. That spending is reported separately and is often the larger number.</li>
    <li><strong>Timing.</strong> Large late contributions show up in the 48-hour reports, not the monthly ones.</li>
  </ul>

  <h2>If something looks wrong</h2>
  <p>Complaints about campaign finance reports go to the Secretary of State's office, which can fine late or incomplete filers and refer violations for enforcement.</p>
""",
    sources=[("https://voteidaho.gov/campaign-finance-portal/", "Campaign Finance 101, with links to every search site (Idaho Secretary of State)"),
             ("https://sunshine.voteidaho.gov/", "Sunshine Portal (Idaho Secretary of State)"),
             ("https://archive.voteidaho.gov/download/cf_guide_state.pdf", "Campaign finance guide for state office candidates (Idaho Secretary of State)"),
             ("https://ballotpedia.org/Campaign_finance_in_Idaho", "Campaign finance in Idaho (Ballotpedia)"),
             ("https://www.fec.gov/", "Federal Election Commission")])

G["state-agencies"] = dict(
    cat="State", title="Which state agency does what",
    lede="A short directory for the most common needs, and what to do when you can't get an answer.",
    body="""
  <h2>Everyday needs</h2>
  <ul>
    <li><strong>Health coverage, food assistance, child support, child protection:</strong> <a href="https://healthandwelfare.idaho.gov/" rel="noopener">Department of Health and Welfare</a>. Dialing 2-1-1 reaches the Idaho CareLine, which connects people to health and human services statewide.</li>
    <li><strong>Unemployment, job search, unpaid wages:</strong> <a href="https://www.labor.idaho.gov/" rel="noopener">Department of Labor</a>.</li>
    <li><strong>Driver's licenses and vehicle registration:</strong> <a href="https://itd.idaho.gov/" rel="noopener">Idaho Transportation Department</a> sets the rules and offers online services. In person, licenses are handled at county sheriff's offices and registration at county assessor's offices.</li>
    <li><strong>State income tax, sales tax, property tax relief:</strong> <a href="https://tax.idaho.gov/" rel="noopener">State Tax Commission</a>.</li>
    <li><strong>Scams, bad business practices, open meetings and public records questions:</strong> <a href="https://www.ag.idaho.gov/" rel="noopener">Attorney General</a>.</li>
    <li><strong>Insurance complaints:</strong> <a href="https://doi.idaho.gov/" rel="noopener">Department of Insurance</a>.</li>
    <li><strong>Professional and contractor licenses, and complaints about a licensed professional:</strong> <a href="https://dopl.idaho.gov/" rel="noopener">Division of Occupational and Professional Licenses</a>.</li>
    <li><strong>Discrimination at work, in housing or in public places:</strong> <a href="https://humanrights.idaho.gov/" rel="noopener">Idaho Human Rights Commission</a>.</li>
    <li><strong>Voting, elections, business filings:</strong> <a href="https://voteidaho.gov/" rel="noopener">Secretary of State</a>.</li>
  </ul>

  <h2>Land, water and the outdoors</h2>
  <ul>
    <li><strong>Hunting and fishing licenses, wildlife:</strong> <a href="https://idfg.idaho.gov/" rel="noopener">Department of Fish and Game</a>.</li>
    <li><strong>State parks, boat and off-road vehicle stickers:</strong> <a href="https://parksandrecreation.idaho.gov/" rel="noopener">Department of Parks and Recreation</a>.</li>
    <li><strong>Water rights and wells:</strong> <a href="https://idwr.idaho.gov/" rel="noopener">Department of Water Resources</a>.</li>
    <li><strong>Air and water quality, spills:</strong> <a href="https://www.deq.idaho.gov/" rel="noopener">Department of Environmental Quality</a>.</li>
    <li><strong>Electric, gas and water utility rates:</strong> <a href="https://puc.idaho.gov/" rel="noopener">Public Utilities Commission</a>, which takes public comment on rate cases.</li>
  </ul>
  <p>About two-thirds of Idaho is federal land. National forests, Bureau of Land Management ground and national parks are run by federal agencies, not the state. See <a href="federal-agencies.html">working with federal agencies</a>.</p>

  <h2>Schools and public safety</h2>
  <ul>
    <li><strong>K-12 schools:</strong> your local school district first, then the <a href="https://www.sde.idaho.gov/" rel="noopener">State Department of Education</a>.</li>
    <li><strong>Colleges and universities:</strong> the <a href="https://boardofed.idaho.gov/" rel="noopener">State Board of Education</a>.</li>
    <li><strong>State prisons, probation and parole:</strong> <a href="https://www.idoc.idaho.gov/" rel="noopener">Department of Correction</a>. County jails are run by the sheriff.</li>
    <li><strong>State highways and troopers:</strong> the Transportation Department and the <a href="https://isp.idaho.gov/" rel="noopener">Idaho State Police</a>.</li>
  </ul>

  <h2>When you're stuck</h2>
  <ol>
    <li><strong>Ask for a supervisor, and get names and dates in writing.</strong></li>
    <li><strong>Use the agency's formal process.</strong> Most decisions about benefits, licenses and permits come with a right to appeal and a deadline. The deadline is on the notice.</li>
    <li><strong>Call your legislators.</strong> They can ask an agency about a constituent's case. See <a href="../reps.html">Who represents you</a>.</li>
    <li><strong>Contact the Governor's office,</strong> which takes constituent requests about state agencies.</li>
    <li><strong>Ask for the records.</strong> You can request your own file, or any public record, under the Public Records Act.</li>
  </ol>

  <h2>Rules, not just laws</h2>
  <p>Agencies write rules that fill in the details of state law. Proposed rules are published in the monthly Idaho Administrative Bulletin with a public comment period, and the Legislature reviews them each session. If a rule is the problem, that comment period is the time to say so.</p>
""",
    sources=[("https://www.idaho.gov/", "Idaho.gov, the state's official website and agency directory"),
             ("https://gov.idaho.gov/contact/contact-us/", "Contact the Governor's office"),
             ("https://www.ag.idaho.gov/content/uploads/2026/07/PublicRecordsLaw.pdf", "Idaho Public Records Law Manual, July 2026 (Idaho Attorney General)")])

G["running-for-office"] = dict(
    cat="State", title="Running for office",
    lede="Idaho has thousands of elected seats, most of them local and many uncontested. Here is which offices are up when, how filing works and what the money rules are.",
    body="""
  <h2>Which offices are up when</h2>
  <ul>
    <li><strong>Even years, partisan:</strong> all 105 seats in the Legislature, county commissioners and other county officers, and Idaho's two seats in the U.S. House. Party primaries are on the third Tuesday in May and the general election is in November.</li>
    <li><strong>Every four years (2026, 2030):</strong> Governor, Lieutenant Governor, Secretary of State, Controller, Treasurer, Attorney General and Superintendent of Public Instruction.</li>
    <li><strong>Odd years, nonpartisan:</strong> mayors, city councils and school board trustees, in November.</li>
    <li><strong>Judges</strong> run without party labels. Supreme Court, Court of Appeals and district judges are on the May ballot.</li>
    <li><strong>Special districts,</strong> such as highway, fire, library and cemetery districts, elect their boards on set election dates in May or November. Your county clerk knows which.</li>
    <li><strong>Precinct committeemen,</strong> the entry-level party office, are elected in the May primary of even years. There is no fee to file.</li>
  </ul>

  <h2>Who can run</h2>
  <p>For most offices you must be a registered voter living in the district you want to represent. Some offices add requirements: legislators must have lived in their district for a year, the Governor must be at least 30, and prosecutors and judges must be lawyers. The Secretary of State's candidate pages list the rules for each office.</p>
  <p>A registered voter is a U.S. citizen, at least 18, who has lived in Idaho and the county for at least 30 days and has registered (Idaho Code 34-402). Permanent residents (green card holders) and other noncitizens can't register, so they can't vote, sign petitions or run for these offices.</p>

  <h2>Filing</h2>
  <ul>
    <li><strong>Where:</strong> federal, statewide, legislative and judicial candidates file with the Secretary of State. County candidates file with the county clerk, city candidates with the city clerk, and district candidates with the district or the county clerk.</li>
    <li><strong>When:</strong> for the May primary, filing runs for about two weeks in late February and early March. City and school board candidates file in late summer of odd years. The exact dates are set each cycle, and the deadline is firm.</li>
    <li><strong>Fee or signatures:</strong> most partisan offices let you pay a filing fee or turn in petition signatures instead. In 2026 the fee was $30 for the Legislature and $40 for county commissioner, against 50 and 5 signatures. Independent candidates must file by petition.</li>
    <li><strong>Write-ins</strong> must file a declaration of intent or their votes aren't counted.</li>
  </ul>

  <h2>Party primaries</h2>
  <p>Each party decides who can vote in its primary. The Republican primary is open only to voters registered as Republicans, and in most of Idaho the Republican primary decides the race. If you want a say in it, check your registration well ahead. The deadline to switch from one party to another comes months before the May primary, when candidate filing closes.</p>

  <h2>Money</h2>
  <ul>
    <li><strong>Track everything from day one,</strong> including your own money.</li>
    <li><strong>Name a political treasurer before you take or spend any money.</strong> Every candidate must appoint a treasurer and give the treasurer's name and address to the Secretary of State before receiving a contribution or making an expenditure (Idaho Code 67-6603). You can be your own treasurer.</li>
    <li><strong>Open a separate campaign bank account.</strong> Since July 1, 2026 (House Bill 930), campaign money has to go in its own checking account and can't be mixed with any other money. If you lend your campaign more than $1,000 of your own money, the loan has to go into that account and be reported. Campaign money can be invested only in cash accounts such as CDs or money market accounts, not stocks.</li>
    <li><strong>Know when reports start.</strong> Candidates for judicial and local offices don't have to file reports until they raise or spend $500 (Idaho Code 67-6608). Other candidates have no such threshold. A group that takes in and spends more than $1,000 in a year to support or oppose candidates or measures is a political committee, with its own treasurer and reports (Idaho Code 67-6602).</li>
    <li><strong>Report online</strong> through the Secretary of State's Sunshine Portal, at every level of office.</li>
    <li><strong>Know the limits.</strong> The Secretary of State's guides list $1,000 per donor per election for legislative races and $5,000 for statewide ones. Confirm the current figures before you raise money.</li>
  </ul>
  <p>See <a href="campaign-finance.html">following the money in Idaho politics</a>.</p>

  <h2>Where to start</h2>
  <ul>
    <li><strong>Call your county clerk's elections office.</strong> They'll tell you which seats are up, when filing opens and what forms you need.</li>
    <li><strong>Go to the meetings</strong> of the board you'd join. The <a href="../">calendar</a> lists many of them.</li>
    <li><strong>Consider an appointed seat first.</strong> See <a href="boards-and-commissions.html">serve on a board or commission</a>.</li>
  </ul>
""",
    sources=[("https://voteidaho.gov/?p=2486", "How to run for office, with fees and signature counts for every office (Idaho Secretary of State)"),
             ("https://voteidaho.gov/candidate-filing/", "Candidate filing (Idaho Secretary of State)"),
             ("https://voteidaho.gov/county-clerk/", "County elections offices (Idaho Secretary of State)"),
             ("https://archive.voteidaho.gov/download/cf_guide_local.pdf", "Campaign finance guide for local office candidates (Idaho Secretary of State)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title67/T67CH66/SECT67-6603/", "Idaho Code 67-6603, political treasurer (Idaho Legislature)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title67/T67CH66/SECT67-6608/", "Idaho Code 67-6608, the $500 reporting threshold for judicial and local candidates (Idaho Legislature)"),
             ("https://legislature.idaho.gov/sessioninfo/2026/legislation/H0930", "House Bill 930 (2026), campaign accounts and candidate loans (Idaho Legislature)"),
             ("https://sunshine.voteidaho.gov/", "Sunshine Portal (Idaho Secretary of State)")])

G["state-initiatives"] = dict(
    cat="State", title="State initiatives and referendums",
    lede="Idaho voters can write state laws themselves and can overturn laws the Legislature passes. The signature rules are among the toughest in the West. Here is how each path works.",
    body="""
  <h2>Two paths for voters</h2>
  <ul>
    <li><strong>Initiative.</strong> Voters propose a new law or a change to an existing one. With enough signatures it goes on the November ballot in an even-numbered year.</li>
    <li><strong>Referendum.</strong> Voters ask to overturn a law the Legislature just passed. The petition has to be filed within 60 days after the session ends.</li>
  </ul>
  <p>Initiatives in Idaho can change state law only. Voters cannot propose amendments to the Idaho Constitution. Those have to come from the Legislature.</p>

  <h2>How many signatures</h2>
  <ul>
    <li><strong>Six percent of registered voters statewide,</strong> counted as of the last general election.</li>
    <li><strong>And six percent in each of at least 18 of the 35 legislative districts.</strong> Signatures from Boise alone can't qualify a measure.</li>
  </ul>
  <p>The Secretary of State publishes the exact numbers for each cycle. Campaigns collect well over the minimum, because county clerks strike signatures that don't match a registered voter at that address.</p>

  <h2>The steps</h2>
  <ol class="steps">
    <li><strong>Start with 20 signatures.</strong> Sponsors file the proposed text with the Secretary of State along with the signatures of 20 registered voters and a proposed way to pay for it.</li>
    <li><strong>Review.</strong> The Attorney General reviews the text and can suggest changes, which sponsors are free to ignore. The state budget office writes a fiscal impact statement.</li>
    <li><strong>Ballot titles.</strong> The Attorney General writes a short and a long title. Anyone unhappy with them can appeal to the Idaho Supreme Court within 20 days.</li>
    <li><strong>Circulation.</strong> Sponsors have up to 18 months, ending April 30 of the election year. Circulators must be Idaho residents at least 18 years old, and each signature sheet covers one county.</li>
    <li><strong>County clerks verify.</strong> Signatures go to the county clerks by May 1, and the clerks have until the end of June to check them.</li>
    <li><strong>The ballot.</strong> A measure with enough valid signatures goes on the November ballot and passes with a simple majority.</li>
  </ol>

  <h2>If you're asked to sign</h2>
  <ul>
    <li><strong>You can read it first.</strong> The circulator must show you the ballot titles and offer you a copy of the measure and its fiscal impact summary.</li>
    <li><strong>You must be a qualified voter:</strong> a U.S. citizen, at least 18, living in Idaho and your county for at least 30 days, and registered to vote (Idaho Code 34-402). Permanent residents (green card holders) and other noncitizens can't sign. You sign with your own name and address.</li>
    <li><strong>You can change your mind.</strong> You can take your name off before the petition goes to the county clerk, or ask the clerk in writing before signatures are verified.</li>
    <li><strong>Signing isn't voting.</strong> It only says the question should be on the ballot.</li>
  </ul>

  <h2>After an initiative passes</h2>
  <p>A law passed by initiative is an ordinary state law. The Legislature can amend or repeal it at any time with a simple majority, and it has done so.</p>

  <h2>Measures the Legislature sends you</h2>
  <ul>
    <li><strong>Constitutional amendments.</strong> These need a two-thirds vote in both the House and the Senate, then a majority of voters at the next general election.</li>
    <li><strong>Advisory questions.</strong> The Legislature sometimes asks voters a non-binding question.</li>
  </ul>

  <h2>How to weigh in</h2>
  <ul>
    <li><strong>Read the voters' pamphlet</strong> the Secretary of State mails before the general election, with each measure's text and arguments for and against.</li>
    <li><strong>Check who is funding each side</strong> through the <a href="campaign-finance.html">Sunshine Portal</a>.</li>
  </ul>
""",
    sources=[("https://voteidaho.gov/initiative-filing-requirements/", "Initiative filing requirements (Idaho Secretary of State)"),
             ("https://voteidaho.gov/?p=3109", "Initiatives and amendments, current and past (Idaho Secretary of State)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/", "Idaho Code Title 34, Chapter 18, Initiative and Referendum Elections (Idaho Legislature)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/title34/t34ch4/sect34-402", "Idaho Code 34-402, who can vote (Idaho Legislature)"),
             ("https://legislature.idaho.gov/statutesrules/idconst/", "Idaho Constitution, Article III, Section 1 and Article XX (Idaho Legislature)")])

G["federal-offices"] = dict(
    cat="Federal", title="Federal elections and who can run",
    lede="Idaho sends four people to Congress and helps elect a President. Here is who can run for each office and how often.",
    body="""
  <h2>The offices</h2>
  <ul>
    <li><strong>U.S. House of Representatives.</strong> Idaho has two House members, each elected from a congressional district for a two-year term. The 1st District covers the north and west, including the Panhandle and Canyon County. The 2nd covers the east and south, including most of Boise. Both seats are on the ballot in every even-numbered year.</li>
    <li><strong>U.S. Senate.</strong> Idaho has two senators, elected statewide for six-year terms. Their terms are staggered, so the seats come up in different years.</li>
    <li><strong>President and Vice President.</strong> Elected every four years. Idaho has four electoral votes, and all four go to the ticket that wins the state's popular vote.</li>
  </ul>

  <h2>Who can run (set by the U.S. Constitution)</h2>
  <ul>
    <li><strong>House:</strong> at least 25 years old, a U.S. citizen for at least seven years, and a resident of the state. Members don't have to live in the district they represent.</li>
    <li><strong>Senate:</strong> at least 30 years old, a U.S. citizen for at least nine years, and a resident of the state.</li>
    <li><strong>President:</strong> at least 35 years old, a natural-born citizen, and a U.S. resident for at least 14 years. No one can be elected President more than twice.</li>
  </ul>

  <h2>How Idaho runs these elections</h2>
  <ul>
    <li><strong>House and Senate</strong> candidates are nominated in party primaries on the third Tuesday in May. Each party decides who can vote in its primary, and the Republican primary is open only to registered Republicans. The winners face each other in November.</li>
    <li><strong>Presidential nominations</strong> are run by the parties. In 2024 Idaho held no state-run presidential primary, and both major parties used caucuses. Check with your party or the Secretary of State for how 2028 will work.</li>
    <li><strong>Candidates for Congress</strong> file with the Idaho Secretary of State during the late-winter filing period. In 2026 the fee was $500 for the Senate and $300 for the House, or petition signatures instead. They report campaign money to the Federal Election Commission, not the state.</li>
  </ul>

  <h2>How to follow your members</h2>
  <ul>
    <li><strong>Find them</strong> with <a href="../reps.html">Who represents you</a>.</li>
    <li><strong>Track their votes and bills</strong> on Congress.gov.</li>
    <li><strong>See who funds their campaigns</strong> at the Federal Election Commission's website, fec.gov.</li>
    <li><strong>Use their Idaho offices.</strong> Each member has staff in several Idaho cities who help with federal agencies. See <a href="federal-agencies.html">working with federal agencies</a>.</li>
  </ul>
""",
    sources=[("https://constitution.congress.gov/constitution/", "The Constitution of the United States (Congress.gov)"),
             ("https://legislature.idaho.gov/legislators/congressional-delegation/", "Idaho's congressional delegation (Idaho Legislature)"),
             ("https://voteidaho.gov/?p=2486", "How to run for office (Idaho Secretary of State)"),
             ("https://www.congress.gov/", "Congress.gov"),
             ("https://www.fec.gov/", "Federal Election Commission")])

G["courts"] = dict(
    cat="Federal and state", title="How the courts work",
    lede="Most people meet the courts through a traffic ticket, a family matter, a small claim or jury duty. Here is how Idaho's courts and the federal courts are set up, side by side.",
    body="""
  <h2>Idaho's state courts</h2>
  <p>Idaho has one unified court system, run by the Idaho Supreme Court, with a courthouse in every county. Almost every case starts in a district court.</p>
  <ul>
    <li><strong>Magistrate division.</strong> Part of the district court, and where most people end up. Magistrate judges handle traffic tickets and infractions, misdemeanors, the first hearings in felony cases, small claims, civil cases up to $10,000, evictions, divorce and custody, juvenile cases, probate and guardianships.</li>
    <li><strong>District judges.</strong> They hear felony trials, civil cases over $10,000 and appeals from the magistrate division. The state is divided into seven judicial districts.</li>
    <li><strong>Court of Appeals.</strong> Four judges, sitting in panels of three, hear appeals the Supreme Court assigns to them. They review the record. There are no new trials or witnesses.</li>
    <li><strong>Supreme Court.</strong> Five justices. It is the last word on Idaho law, and it also writes the court rules and oversees lawyers.</li>
  </ul>

  <h2>How Idaho's judges get there</h2>
  <ul>
    <li><strong>Justices, appeals judges and district judges are elected</strong> without party labels, on the May ballot. Supreme Court and Court of Appeals terms are six years and district judges' terms are four.</li>
    <li><strong>In practice most are first appointed.</strong> When a judge leaves mid-term, the Governor appoints a replacement from a list of nominees, and that judge then stands for election.</li>
    <li><strong>Magistrate judges are appointed</strong> by a commission in each judicial district and then face a yes-or-no retention vote.</li>
  </ul>

  <h2>The federal courts</h2>
  <ul>
    <li><strong>U.S. District Court for the District of Idaho.</strong> The trial court for federal crimes, cases under federal law or the U.S. Constitution, bankruptcy, and some disputes between people from different states.</li>
    <li><strong>Ninth Circuit Court of Appeals.</strong> Hears appeals from Idaho and eight other western states.</li>
    <li><strong>U.S. Supreme Court.</strong> Takes a small share of the cases it is asked to hear.</li>
  </ul>
  <p>Federal judges are nominated by the President, confirmed by the Senate and serve for life.</p>

  <h2>Tribal courts</h2>
  <p>Idaho's five federally recognized tribes, the Coeur d'Alene, Kootenai, Nez Perce, Shoshone-Bannock and Shoshone-Paiute, are sovereign governments with their own courts and laws.</p>

  <h2>Where you fit in</h2>
  <ul>
    <li><strong>Watch.</strong> Court hearings are open to the public, with narrow exceptions such as juvenile cases.</li>
    <li><strong>Look up a case.</strong> Idaho's iCourt Portal has public case records from every county.</li>
    <li><strong>Get help without a lawyer.</strong> The Court Assistance Office provides forms and guidance for people representing themselves, with an office in most courthouses.</li>
    <li><strong>Serve on a jury.</strong> Names are drawn from voter registration and driver's license lists. Jurors must be U.S. citizens, at least 18, and live in the county (Idaho Code 2-209). Because driver's license lists include people who aren't citizens, a noncitizen can still get a summons. Don't ignore it: respond to the court and say that you are not a U.S. citizen. Employers can't fire you for serving.</li>
    <li><strong>Vote.</strong> Judges are on your ballot. Contested races are rare, which makes the ones that happen matter more. Only U.S. citizens who are at least 18 and registered can vote in Idaho (Idaho Code 34-402).</li>
  </ul>
""",
    sources=[("https://isc.idaho.gov/about-the-courts", "About the courts (Idaho Supreme Court)"),
             ("https://archive.sos.idaho.gov/blue_book/blue_book_2025-2026.pdf", "The Blue Book of Idaho, 2025-2026, judicial branch section (Idaho Secretary of State)"),
             ("https://courtselfhelp.idaho.gov/", "Court Assistance Office (Idaho Supreme Court)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title2/T2CH2/SECT2-209", "Idaho Code 2-209, juror qualifications (Idaho Legislature)"),
             ("https://www.uscourts.gov/about-federal-courts", "About federal courts (United States Courts)")])

G["constitution"] = dict(
    cat="Federal and state", title="Understanding the Constitution",
    lede="You live under two constitutions: the United States Constitution and Idaho's. Here is what each one does and how each one changes.",
    body="""
  <h2>The U.S. Constitution</h2>
  <ul>
    <li><strong>It sets up the federal government:</strong> Congress, the President and the federal courts, each checking the others.</li>
    <li><strong>It divides power</strong> between the federal government and the states.</li>
    <li><strong>It protects individual rights,</strong> mostly through its amendments. The first ten are the Bill of Rights. Later ones ended slavery, guaranteed equal protection and due process, and extended the vote.</li>
  </ul>

  <h2>The Idaho Constitution</h2>
  <ul>
    <li><strong>It dates from statehood.</strong> Delegates wrote it in Boise in the summer of 1889, voters approved it that fall, and Idaho became a state on July 3, 1890.</li>
    <li><strong>It is longer and more specific</strong> than the federal one. It covers schools, water rights, taxes, public lands, counties and cities.</li>
    <li><strong>Article I is Idaho's own declaration of rights.</strong> State constitutions can protect more than the federal one does, and Idaho's includes rights the federal Constitution doesn't spell out, such as crime victims' rights and the right to hunt, fish and trap.</li>
    <li><strong>It limits the government in practical ways:</strong> the budget has to balance, most local government debt needs a two-thirds vote of the people, and the Legislature has to maintain a "general, uniform and thorough" system of free public schools.</li>
    <li><strong>It reserves power to the voters:</strong> the initiative, the referendum and the recall are all in the constitution.</li>
  </ul>

  <h2>How each one changes</h2>
  <ul>
    <li><strong>U.S. Constitution:</strong> an amendment needs two-thirds of both houses of Congress, then approval by three-quarters of the states. It has been amended 27 times.</li>
    <li><strong>Idaho Constitution:</strong> an amendment needs two-thirds of both the House and the Senate, then a majority of voters at the next general election. Voters can't propose amendments by initiative.</li>
  </ul>
  <p>That means every change to Idaho's constitution comes to you as a ballot question, usually labeled HJR or SJR with a number. See <a href="state-initiatives.html">state initiatives and referendums</a>.</p>

  <h2>Who decides what it means</h2>
  <p>Courts do, case by case. The U.S. Supreme Court has the last word on the federal Constitution, and the Idaho Supreme Court has the last word on Idaho's. See <a href="courts.html">how the courts work</a>.</p>

  <h2>Reading them yourself</h2>
  <p>Both are short enough to read in an evening. The Legislature's website has the full Idaho Constitution, article by article, and Congress.gov has the U.S. Constitution with plain-language notes on each clause.</p>
""",
    sources=[("https://legislature.idaho.gov/statutesrules/idconst/", "Constitution of the State of Idaho (Idaho Legislature)"),
             ("https://constitution.congress.gov/constitution/", "The Constitution of the United States, annotated (Congress.gov)"),
             ("https://www.archives.gov/founding-docs/constitution", "The Constitution (National Archives)")])

G["federal-agencies"] = dict(
    cat="Federal", title="Working with federal agencies",
    lede="When a federal agency is stuck, slow or about to make a decision that affects you, there are ways to get through. In Idaho, where the federal government manages most of the land, that comes up often.",
    body="""
  <h2>When you're stuck with an agency</h2>
  <p><strong>Ask your member of Congress for help.</strong> Every House and Senate office has caseworkers who help constituents with federal agencies, including Social Security, Medicare, veterans' benefits, the IRS, passports and immigration cases.</p>
  <ul>
    <li><strong>Call or fill out the office's online form.</strong> Find your members with <a href="../reps.html">Who represents you</a>. Each has offices around Idaho.</li>
    <li><strong>Expect to sign a privacy release,</strong> which lets the agency share your case with the office.</li>
    <li><strong>Bring case numbers and copies of letters.</strong></li>
  </ul>

  <h2>Public land decisions</h2>
  <p>The Forest Service and the Bureau of Land Management manage most of Idaho's land. Grazing permits, timber sales, travel plans, mining and fire projects all go through public review.</p>
  <ul>
    <li><strong>Each forest and BLM district posts its projects</strong> and takes comments, usually for 30 days or more.</li>
    <li><strong>Get on the mailing list</strong> for the forest or district near you, so notices reach you while comments are open.</li>
    <li><strong>Comment early and specifically.</strong> On many projects, only people who commented can object later.</li>
    <li><strong>Local advisory groups,</strong> such as BLM resource advisory councils, have seats for residents.</li>
  </ul>

  <h2>Comment on a proposed rule</h2>
  <p>Federal agencies write regulations that carry out laws. Before most rules are final, the agency publishes a proposal and takes public comments.</p>
  <ul>
    <li><strong>Find proposed rules</strong> in the Federal Register.</li>
    <li><strong>Comment on Regulations.gov</strong> before the deadline.</li>
    <li><strong>Be specific.</strong> Agencies have to consider the substance of comments, not count them. Explain how the rule would affect you, and suggest a change.</li>
  </ul>

  <h2>Request records</h2>
  <p>The Freedom of Information Act lets anyone request records from federal agencies. FOIA.gov explains how and links to each agency's request page. Some records are exempt, like classified information and private personal details.</p>

  <h2>Report a problem</h2>
  <ul>
    <li><strong>Most agencies have an Inspector General</strong> who investigates fraud, waste and abuse, and takes tips from the public.</li>
    <li><strong>Many agencies also have an ombudsman</strong> who helps resolve complaints.</li>
  </ul>
""",
    sources=[("https://www.regulations.gov/", "Regulations.gov"),
             ("https://www.federalregister.gov/", "Federal Register"),
             ("https://www.foia.gov/", "FOIA.gov"),
             ("https://legislature.idaho.gov/legislators/congressional-delegation/", "Idaho's congressional delegation (Idaho Legislature)")])

G["federal-budget"] = dict(
    cat="Federal", title="The federal budget and where you can weigh in",
    lede="The federal budget funds things Idaho depends on, from national forests and highways to veterans' care and the Idaho National Laboratory. Here is how it gets made and where public input fits.",
    body="""
  <h2>Two kinds of spending</h2>
  <ul>
    <li><strong>Mandatory spending</strong> is set by existing law and doesn't need a vote each year. It includes Social Security, Medicare and most of Medicaid. It is the larger share.</li>
    <li><strong>Discretionary spending</strong> is decided each year by Congress through appropriations bills. It covers defense and most federal agencies, grants and programs.</li>
  </ul>

  <h2>The yearly cycle</h2>
  <ul>
    <li><strong>The fiscal year</strong> runs from October 1 to September 30.</li>
    <li><strong>Early in the year,</strong> the President sends Congress a budget request. It is a proposal, not law.</li>
    <li><strong>Spring and summer:</strong> House and Senate appropriations subcommittees write the annual spending bills, usually 12 of them, each covering a group of agencies.</li>
    <li><strong>By October 1,</strong> Congress is supposed to pass them. When it doesn't, it usually passes a continuing resolution to keep funding at current levels. If neither passes, parts of the government shut down.</li>
  </ul>

  <h2>Where you can weigh in</h2>
  <ul>
    <li><strong>Contact your members of Congress</strong> about programs you care about, especially in the spring, while appropriations bills are being written.</li>
    <li><strong>Local projects.</strong> Members of Congress can request funding for specific community projects in their district or state. Local governments, nonprofits and tribes ask their members, usually in late winter or early spring. Check your members' websites for their process and deadlines.</li>
    <li><strong>Public witness testimony.</strong> Some appropriations subcommittees accept written testimony from the public.</li>
    <li><strong>Federal money often flows through the state.</strong> Medicaid, highway funds and many grants pass through Idaho agencies, and the Legislature decides whether and how to spend them. See <a href="state-budgets.html">the state budget and how to influence it</a>.</li>
  </ul>

  <h2>Following the money</h2>
  <p>The Congressional Budget Office publishes plain-language overviews of the budget, and USAspending.gov shows where federal money goes, down to the county.</p>
""",
    sources=[("https://www.cbo.gov/topics/budget", "The federal budget (Congressional Budget Office)"),
             ("https://www.usaspending.gov/", "USAspending.gov"),
             ("https://www.congress.gov/", "Congress.gov")])
