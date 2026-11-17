"""Guides added November 2026: public records and the Open Meeting Law."""
G = {}

PRM = "https://www.ag.idaho.gov/content/uploads/2026/07/PublicRecordsLaw.pdf"
OML = "https://www.ag.idaho.gov/content/uploads/2026/07/OpenMeeting.pdf"

G["public-records-requests"] = dict(
    cat="Local", title="How to request public records in Idaho",
    lede="Emails, contracts, budgets, police reports, meeting packets: most of what Idaho governments write down belongs to the public. Here's how to ask for it, what it costs, how fast you should hear back, and what to do if they say no.",
    body="""
  <h2>What you can ask for</h2>
  <p>A public record is any writing about public business that a state or local agency prepares, owns, uses or keeps, in any form: paper, email, text messages, spreadsheets, photos, recordings (Idaho Code &sect; 74-101(13)). The law covers state agencies, the Legislature and the courts' administrative records, and every local agency: counties, cities, school districts and special districts (&sect; 74-101).</p>
  <p>Anyone can ask (&sect; 74-102(1)). In general an agency can't ask you why you want the records. It also doesn't have to create a record that doesn't already exist, so ask for documents, not answers to questions.</p>

  <h2>How to make a request</h2>
  <ol>
    <li><strong>Find the records custodian.</strong> Every agency must name at least one (&sect; 74-102(16)). Search the agency's website for "public records request." Many have an online form. Send your request to the custodian: a request sent to the wrong person may not start the clock (&sect; 74-103(1)).</li>
    <li><strong>Put it in writing.</strong> Email is fine (&sect; 74-102(4)). Say clearly that it's a public records request.</li>
    <li><strong>Describe the records specifically,</strong> with a date range. "Emails between the city administrator and the parks director about the Main Street park, Jan. 1 to March 31, 2026" gets a faster, cheaper answer than "everything about the park."</li>
    <li><strong>Include your contact information.</strong> The law asks for your name, mailing address, email and phone number, and a written statement of whether you are an Idaho resident (&sect; 74-102(4)). Residency changes the deadlines and fees below. It means living in Idaho for at least 30 days in a row (&sect; 74-101(15)).</li>
    <li><strong>Say how you want them.</strong> If the records exist electronically, you can ask for electronic copies (&sect; 74-102(15)). You can also ask to inspect records in person instead of buying copies.</li>
  </ol>
  <div class="callout">
    <p><strong>A simple request</strong></p>
    <p>"This is a public records request under Idaho Code &sect; 74-102. Please provide electronic copies of [describe the records] from [start date] to [end date]. I am / am not an Idaho resident. My contact information: [name, mailing address, email, phone]. If any part of this request is denied, please cite the specific exemption and release the rest of the record with the exempt parts redacted."</p>
  </div>

  <h2>How fast they have to answer</h2>
  <ul>
    <li><strong>Idaho residents:</strong> the agency has <strong>3 working days</strong> to grant or deny. If it needs longer to find or copy the records, it must tell you in writing and provide them within <strong>10 working days</strong> (&sect; 74-103(2)).</li>
    <li><strong>Non-residents:</strong> 21 days, extendable to 35 (&sect; 74-103(2)).</li>
    <li>If the deadline passes with no answer, the request is treated as denied (&sect; 74-103(3)), and you can go to court (below).</li>
  </ul>

  <h2>What it costs</h2>
  <ul>
    <li><strong>For Idaho residents, the first two hours of work and the first 100 pages of copies are free</strong> (&sect; 74-102(10)(a)). After that, agencies may charge their actual copy costs and staff time at the rate of the lowest-paid employee who can do the work.</li>
    <li>Charges must be itemized: per-page costs, hourly rate and actual time. No lump sums (&sect; 74-102(10)(h)).</li>
    <li>The agency may ask for a deposit before it starts, and must refund anything it doesn't use (&sect; 74-102(12)).</li>
    <li><strong>Fee waivers:</strong> fees must be waived when the records will significantly help the public understand government, the request isn't mainly for your own benefit, and the cost would keep you from getting them (&sect; 74-102(10)(f)). Ask for a waiver in your request if that fits.</li>
    <li>Non-residents can be charged actual costs from the first page.</li>
  </ul>
  <p>Tip: asking for electronic copies, or inspecting in person, usually costs less than paper.</p>

  <h2>What they can hold back</h2>
  <p>The law lists exemptions, and agencies must read them narrowly. When a record has some exempt information in it, the agency has to black out the exempt parts and give you the rest; it can't withhold the whole document for that reason alone. Common exemptions:</p>
  <ul>
    <li><strong>Personnel records,</strong> except that every public employee's job title, pay, employment history and workplace are public (&sect; 74-106(1)).</li>
    <li><strong>Active law enforcement investigations,</strong> to the extent release would interfere with them, endanger someone or invade privacy. Basic facts of an incident and an arrest are still public, and more opens up once an investigation is inactive (&sect; 74-124).</li>
    <li><strong>Personal identifiers</strong> such as Social Security numbers (&sect; 74-106).</li>
    <li><strong>Legal advice and litigation records,</strong> trade secrets, and appraisals or bid estimates before a deal or bid opening (&sect;&sect; 74-104, 74-107).</li>
  </ul>
  <p>Records about yourself are different: you can usually see them even if they'd be exempt for someone else, and you can ask the agency to correct them (&sect; 74-113).</p>

  <h2>If they say no</h2>
  <ol>
    <li><strong>Check the denial letter.</strong> A denial must be in writing, cite the specific law it relies on, say whether an attorney reviewed it, and tell you about your right to appeal (&sect; 74-103(4)&ndash;(5)).</li>
    <li><strong>Try narrowing or clarifying.</strong> Many denials and big fee estimates come from requests that are too broad. A phone call to the custodian can fix a lot.</li>
    <li><strong>Go to court if you need to.</strong> You can file a petition in the district court of the county where the records are, within <strong>180 days</strong> of the denial (&sect; 74-115(1)). There's no internal appeal you have to go through first. The court must set a hearing within 28 days and can look at the records privately to decide. If either side acted frivolously, the court can award attorney fees (&sect; 74-116), and an official who refuses a legitimate request in bad faith can be fined up to $1,000 (&sect; 74-117).</li>
  </ol>
  <p>The Attorney General's office publishes a free manual with the full statute, sample letters and answers to common questions. It's the best single reference, and it's linked below.</p>
""",
    sources=[(PRM, "Idaho Public Records Law Manual, July 2026 edition (Office of the Attorney General)"),
             ("https://www.ag.idaho.gov/office-resources/manuals/", "Attorney General's manuals page"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH1/", "Idaho Code Title 74, Chapter 1: Public Records Act (Idaho Legislature)")])

G["open-meeting-law"] = dict(
    cat="Local", title="Idaho's Open Meeting Law: what it requires",
    lede="When a city council, county commission, school board or other public body meets to decide or discuss public business, Idaho law says the public gets to see it. Here's what that guarantees, what it doesn't, and what you can do when a body gets it wrong.",
    body="""
  <h2>Who it covers</h2>
  <p>The law applies to the governing bodies of state and local agencies: city councils, county commissions, school boards, library and highway district boards, and the commissions and committees that make decisions or recommendations to them (Idaho Code &sect;&sect; 74-202(4)&ndash;(5)). It doesn't cover courts, a single official acting alone, or private groups like nonprofits and homeowners' associations.</p>
  <p>A <strong>meeting</strong> is any gathering of a quorum to make a decision or deliberate toward one, whether it's formal, informal or social (&sect; 74-202(6)). Deliberating includes trading information or opinions about a pending decision. Members can't get around this by meeting in smaller groups or passing views through a go-between, and email or text exchanges among a quorum can count too. The Attorney General's advice to public bodies: "when in doubt, open the meeting."</p>

  <h2>Notice and agendas</h2>
  <ul>
    <li><strong>Regular meetings:</strong> at least 5 calendar days' notice of the meeting and 48 hours' notice of the agenda (&sect; 74-204(1)). Bodies that meet at least monthly can post their yearly schedule instead.</li>
    <li><strong>Special meetings:</strong> at least 24 hours' notice of the meeting and agenda (&sect; 74-204(2)). True emergencies are an exception, and the body has to say what the emergency is at the start of the meeting.</li>
    <li>Notices go up at the agency's office and on its website or social media if it has them.</li>
    <li>Agendas must list the specific topics, and anything the body will vote on must be marked as an <strong>action item</strong> (&sect; 74-204(4)). Adding an item late requires a motion explaining why it wasn't on the agenda, and final action on a late item generally requires an emergency.</li>
  </ul>
  <p>The posted agenda is your best tool: if a vote you care about is coming, it has to show up there first.</p>

  <h2>Executive sessions (closed doors)</h2>
  <p>A body can close part of a meeting only for reasons listed in &sect; 74-206(1), and those reasons are read narrowly. They include:</p>
  <ul>
    <li>Hiring, evaluating or disciplining a specific employee (not general personnel policy).</li>
    <li>Buying property not owned by a public agency.</li>
    <li>Talking with its lawyer about pending or likely litigation.</li>
    <li>Records that are exempt from public disclosure, labor negotiations, and a few others.</li>
  </ul>
  <p>To go into executive session, the body must vote by a <strong>two-thirds roll call</strong>, citing the specific reason, and it can't drift to other topics once inside. <strong>No final decision can be made in executive session</strong> (&sect; 74-206). The vote has to happen in public.</p>

  <h2>What you're entitled to</h2>
  <ul>
    <li><strong>To attend.</strong> Rules for orderly conduct are allowed; rules that make attending practically impossible aren't.</li>
    <li><strong>To record.</strong> You can record open meetings with audio, video or photos, and you can't be removed for doing it (&sect; 74-203(6)).</li>
    <li><strong>Minutes.</strong> Every meeting needs written minutes showing who was there, the motions and the results of votes, available to the public within a reasonable time (&sect; 74-205). No secret ballots (&sect; 74-203(1)).</li>
    <li><strong>A physical place to show up.</strong> Remote meetings are allowed, but at least one member or the agency's chief officer must be at the noticed location so the public can attend (&sect; 74-203(5)).</li>
  </ul>
  <p>What the Open Meeting Law <strong>doesn't</strong> give you is a right to speak. Many bodies hold a public comment period by choice, and other laws require public hearings for things like zoning decisions. See <a href="speak-at-a-public-meeting.html">how to speak at a local public meeting</a>.</p>

  <h2>When a body breaks the law</h2>
  <ol>
    <li><strong>Raise it in writing.</strong> A body that gets written notice of a possible violation has 14 days to respond publicly, and if it agrees, another 14 days to "cure" it by declaring the actions from that meeting void (&sect; 74-208(7)). Many problems get fixed this way.</li>
    <li><strong>Report it.</strong> County prosecutors enforce the law for local bodies; the Attorney General enforces it for state agencies (&sect; 74-208(5)). Members who knowingly violate the law can be fined personally: up to $1,500, or $2,500 for a repeat within a year, and up to $250 for taking part in a noncompliant meeting (&sect; 74-208(2)&ndash;(4)).</li>
    <li><strong>Go to court.</strong> Anyone affected by a violation can sue in the magistrate court of the county where the body meets. A suit to void an action must be filed within <strong>30 days</strong> of the decision; other suits within 180 days of the violation (&sect; 74-208(6)). Private suits can void decisions but can't win penalties or damages.</li>
  </ol>
  <p>The Attorney General's free Open Meeting Law Manual has the full statute and answers to dozens of common questions. It's linked below.</p>
""",
    sources=[(OML, "Idaho Open Meeting Law Manual, July 2026 edition (Office of the Attorney General)"),
             ("https://www.ag.idaho.gov/office-resources/manuals/", "Attorney General's manuals page"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH2/", "Idaho Code Title 74, Chapter 2: Open Meetings Law (Idaho Legislature)")])
