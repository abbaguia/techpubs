---
title: "Rethinking Resilience: What Does It Take to Build Technology We Can Depend On?"
subtitle: "Bridging the Gap Between Rapid Deployment and End-to-End Reliability."
author: "Mahamat Hissein GUIAGOUSSOU"
role: "Developer Community Leader & Senior Cloud and AI Architect"
date: "2026-11-17"
canonical_url: "https://abbaguia.github.io/techpubs/articles/resilience/"
image: "../../assets/images/Rethinking_Resilience_Header_Infographic.jpg"
tags: ["Resilience Engineering", "Cloud Architecture", "AI Infrastructure", "Distributed Systems", "SRE"]
---

![Rethinking Resilience Header Banner](../../assets/images/Rethinking_Resilience_Header_Infographic.jpg)

# Rethinking Resilience: What Does It Take to Build Technology We Can Depend On?
### Bridging the Gap Between Rapid Deployment and End-to-End Reliability. 

By **Mahamat Hissein GUIAGOUSSOU** | Developer Community Leader & Senior Cloud and AI Architect | [LinkedIn Profile](https://www.linkedin.com/in/mahamathisseinguiagoussou/)

---
## Listen to Short Podcast

<div style="background:#1e293b; border:1px solid #334155; border-radius:12px; padding:1.25rem; margin:1.5rem 0; color:#f8fafc;">
  <div style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.08em; color:#38bdf8; margin-bottom:0.25rem;">
    The Mahamat Minute
  </div>
  <div style="font-size:1.1rem; font-weight:600; margin-bottom:0.5rem;">
    How Architectural Flaws Cause System Outages
  </div>
  <audio controls preload="metadata" style="width:100%;">
    <source src="https://objectstorage.us-ashburn-1.oraclecloud.com/n/idmpn7naypvj/b/mmpodcast/o/audio%2F0-En_Short_How_Architectural_Flaws_Cause_System_Outages.mp3" type="audio/mpeg" />
    Your browser does not support the audio element.
  </audio>
</div>

## Listen to All Podcast Editions (EN / FR • Short / Long)

Browse the full [The Mahamat Minute Podcast Hub](https://abbaguia.github.io/techpubs/podcasts/index.html) (Short, Long, English, and French editions), or jump straight to an edition:

## From Manual Provisioning to Intelligent Automation

I remember when provisioning infrastructure for a new project could take several weeks or even a few months. Today, with Infrastructure as Code (IaC), we can provision complex environments through a largely automated process, sometimes with a single click.

Technology continues to evolve. We have moved from centralized computing and traditional infrastructure to distributed systems, cloud computing, and artificial intelligence. Natural-language interfaces and AI agents are beginning to change how we request, provision, and manage technology.

Our ability to build, deploy, and scale systems has changed dramatically.

But has our ability to build systems we can truly depend on evolved at the same pace?

## WHAT: What Does Resilience Really Mean?

We often associate resilience with redundancy, high availability, backups, or disaster recovery. These are important capabilities, but none of them alone guarantees that a service will remain available when something goes wrong.

Resilience is about how a complete system behaves when faced with unexpected conditions: component failures, sudden demand, unavailable dependencies, resource constraints, or events that were not anticipated during design.

A system may have redundant infrastructure and still experience a service disruption. Data may be protected while the application cannot access it. Individual components may remain operational while the complete service is unavailable.

Resilience is not simply about protecting components. It is about protecting the service.

## WHY: Why Does Resilience Matter?

The consequences of failure are not limited to a server going offline or an application returning an error. A disruption can affect customers, business operations, public services, safety, and the people responsible for delivering and supporting those services.

The following experiences, from three telecommunications environments, showed me different ways a service can become vulnerable even when a solution appears technically sound.

### When Success Becomes the Failure Scenario

Early in my career, I worked as a Senior Solution Engineer supporting one of Nigeria’s leading mobile telecommunications operators, serving more than 10 million subscribers.

I proposed a promotional initiative built around temporary, free short-video clips featuring popular actors. At the time, mobile phones had evolved into advanced Java-capable feature phones, predecessors to today’s Android smartphones. Downloadable content consisted mostly of images, ringtones, and Java applications, while short-form video was still relatively new.

During a trial intended to demonstrate the solution’s functionality, the promotion generated close to one million hits in approximately one hour. The trial was not designed to validate production-scale performance or reliability under that level of demand. The application and database were running on the same machine, which became overwhelmed and crashed.

The response was far greater than expected. A successful idea exposed a capacity limitation in the trial environment.

Sometimes, success itself becomes the failure scenario.

### Protecting Components Is Not Enough

A few years earlier, during my first startup experience, I was working as a customer engineer on a project for one of Canada’s largest wireless service providers.

I remember how our field team spent weeks configuring two Sun servers in a data center for the customer to test. One hosted the database and the other the application. We had even named the servers after our daughters.

As we were preparing to leave for the airport after a successful PoC (Proof of Concept), I turned the physical key on the front of one of the Sun servers, thinking I was locking and securing it. Instead, I powered the system down.

We scrambled to bring the environment back online. My colleague was understandably worried about missing his flight, and we barely made it to the airport. Fortunately, this was an isolated trial and quality-assurance environment, so no end-user services were affected.

It was a frustrating moment, but it taught me an important lesson: operational failures do not always come from complex technical defects or malicious actions. Sometimes, a simple and innocent human action can have serious consequences if the environment does not provide the right safeguards.

That lesson becomes even more important in critical environments such as aviation, banking, and healthcare, where connected devices may monitor essential functions, including a patient’s vital signs.

Later, while continuing to support the same Canadian wireless provider in a production setting, I was involved in further improving availability beyond the original separation of the application and database layers. That work improved component-level availability. However, an unexpected mobile content fulfillment transaction flow later revealed resilience weaknesses that could not be addressed by looking at those components individually.

The experience reinforced an important distinction: improving the availability of components in isolation does not automatically make the complete service resilient. The application, data, network, infrastructure, and their dependencies must work together.

### Recognizing a Risk Is Only the First Step

In another engagement with a major wireless provider in the United States, the customer had selected a custom architecture built around a free, open-source, non-clustered version of MySQL, deployed mainly in the context of the customer’s Research & Development (R&D) ecosystem while using our product as their application layer. Our field team identified the database as a single point of failure and raised the concern with the customer.

The customer formally asked Oracle to support an evaluation of Oracle Real Application Clusters (RAC) alternative architecture, to assess how the integrated Oracle Mobile Content Delivery Server would perform with a clustered database backend. The objective was to determine whether the proposed architecture could meet the customer’s end-to-end functional and non-functional requirements for a telecommunications enterprise environment.

This was not simply about database availability. The evaluation needed to consider the complete application experience, including over-the-air application download times, latency, jitter, and the performance requirements of the mobile content-delivery service.

Oracle leadership ultimately made a business decision not to approve the requested free trial. As a result, the customer could not evaluate the proposed RAC-backed architecture within the planned budget for that engagement, and the opportunity did not move forward. Although the requested evaluation did not proceed, the experience highlighted a broader challenge: technical risks can be identified, but addressing them requires organizational alignment, investment, and a willingness to validate alternative approaches.

In the months that followed, Oracle did not secure a more strategic and viable customer for our Mobile Content Delivery product. Meanwhile, the market was changing as Apple and Google introduced and expanded their own competing application-download ecosystems. Oracle eventually discontinued the Mobile Content Delivery Server product.

The discontinuation affected the supporting teams on both sides: at Oracle and at the wireless telecommunications provider.

This experience made the consequences particularly tangible. Resilience is not only about protecting technology and business operations. It also depends on the business decisions, investment, and organizational commitment needed to sustain a solution. Those decisions can ultimately affect people’s livelihoods.

Recognizing a technical risk is important. Having the organizational support to address it is equally important.

### The Common Lesson: Protect the Complete Service

These experiences point to a common lesson: protecting individual components does not necessarily protect the service.

An application can be redundant while its database is not. A storage system can protect data while the application cannot reach it. Infrastructure can remain available while a critical dependency prevents the business service from operating.

A seemingly harmless operational action can also interrupt a service when appropriate safeguards are missing.

Resilience must extend across the complete solution: application, database, network, infrastructure, dependencies, people, and operations.

## Why This Matters Even More Today

Cloud computing and artificial intelligence are increasing the scale, interdependence, and complexity of modern systems. AI workloads place growing demands on compute, networking, storage, power, and data availability.

At the same time, organizations increasingly depend on shared platforms and communications infrastructure for essential operations.

Recent incidents and emerging capacity constraints demonstrate that the effects of a failure can extend well beyond the component where the problem begins.

### Microsoft 365: When a Global Platform Becomes Unavailable

Beginning November 12, 2026, a global Microsoft 365 disruption affected Exchange Online and other services, including Outlook, Teams, Copilot, and related capabilities. Affected users experienced disruption for nearly 24 hours. Microsoft’s preliminary post-incident findings described a combination of factors: a software defect in networking gateway infrastructure, increased traffic following a Teams failover, and reduced server capacity. Together, these conditions contributed to cascading failures across the platform. These findings were preliminary at the time of this article’s preparation.

The incident affected organizations and users worldwide, disrupting access to email and other business functions. It demonstrated how a defect or capacity problem in shared infrastructure can propagate across multiple services and affect organizations that depend on them.

### FAA: When Critical Communications Infrastructure Becomes Unstable

The next day, on November 13, 2026, the Federal Aviation Administration issued a nationwide ground stop for departures at U.S. airports following instability in telecommunications systems supporting air traffic control. The FAA’s preliminary investigation examined excessive traffic entering its telecommunications network during work to transition legacy copper connections to fiber. Officials identified a recently deployed router at a remote communications facility as one possible source of the traffic. Investigators had not established a final root cause at the time of this article’s preparation. The FAA reported instability at 17 of its 22 Air Route Traffic Control Centers. The nationwide ground stop was a precautionary safety measure to protect aircraft and passengers while the affected infrastructure was investigated and stabilized.

This was not a complete loss of radar or radio communications. Aircraft already in the air landed safely, while more than 3,500 flights were grounded during the disruption. The departure restrictions were subsequently lifted.

The incident demonstrated how instability in telecommunications infrastructure can affect critical operations across a national transportation system, even when some communications and safety procedures remain operational.

### Financial Services: When a Transaction Problem Spills Across Institutions

On November 16, 2026, customers reported difficulties accessing online banking services at several major U.S. financial institutions. JPMorgan Chase confirmed that a software bug in its on-premises hardware systems was slowing some transaction processing.

The bank said customers could still access their accounts and funds. It also explained that other financial institutions could experience delays when processing transactions involving JPMorgan. The bank confirmed that its own systems were not directly affected, although some payments involving other institutions could be delayed.

This incident illustrates how a technical problem within one institution can affect transaction flows beyond its own infrastructure. In interconnected financial services, the reliability of a transaction can depend on several organizations and systems working together.

### AI Infrastructure: When Demand Outruns Capacity

A global resilience challenge is emerging across the artificial intelligence industry: the ability to provide enough computing capacity to meet rapidly increasing demand.

Hyperscalers and AI operators are investing heavily in new data centers, advanced processors, networking, storage, and power infrastructure. Their ability to expand, however, is constrained by more than financial investment or the availability of computing equipment.

Access to electricity, grid connections, cooling systems, specialized chips, construction resources, and regulatory approvals can all delay the deployment of new capacity.

There is also a growing public and political dimension. While technology companies and policymakers emphasize the importance of expanding AI infrastructure to maintain competitiveness and support innovation, many communities are pushing back against new data center projects.

Concerns include electricity costs, water consumption, land use, environmental impact, and the broader economic and employment implications of artificial intelligence. Public opposition can influence local permitting decisions and the political environment surrounding data center construction.

The result is a difficult balance: demand for AI computing continues to grow, while the infrastructure required to support that demand cannot always be expanded at the same pace.

This is not simply a future concern. AI providers have already reported periods of constrained computing capacity, slower service, and degraded performance. In a March 2026 incident, Anthropic disclosed that a rapid increase in usage demand, combined with compute constraints in parts of its infrastructure, contributed to a service outage and periods of degraded performance.

A service does not necessarily need to go completely offline to fail its users. When it cannot provide the capacity, response time, or availability that customers expect, it may effectively fail to meet its service requirements.

This is another dimension of resilience: designing systems not only to withstand component failures, but also to operate reliably when demand grows faster than the infrastructure supporting them.

### A Systemic Pattern Across Every Industry

Taken together, these examples show that resilience challenges span cloud productivity platforms, national aviation communications, financial services, and AI infrastructure.

The causes differ, but the engineering questions are familiar: Where are the dependencies? How far can a failure spread? What capacity remains? Can essential services continue operating, and how quickly can they recover?

A problem in one component, organization, or infrastructure layer can affect services and people far beyond its starting point.

These questions must be addressed when systems are designed, not only after an incident occurs.

## The Questions We Must Ask

Building resilient systems starts with asking better questions before implementation:

* What must continue working when something fails?
* Which components and dependencies can become unavailable?
* What happens when demand exceeds expectations?
* Can the system operate in a degraded state?
* How will failures be detected, contained, and recovered from?
* How much performance degradation, data loss, or service interruption can the business tolerate?
* What operational safeguards can prevent human error from becoming a service failure?
* Can the organization sustain the infrastructure, investment, and operational support required over time?

These questions influence architecture, technology choices, deployment, testing, operations, and business decisions.

They also reveal trade-offs. More redundancy can increase cost. Replication can support availability and recovery, but requires additional storage and operational coordination. A design that protects against one type of failure may remain vulnerable to another.

There is no universal architecture that makes every system resilient. The right design depends on what the service must protect, the failures it must tolerate, the demand it must support, and the recovery it must deliver.

## From WHAT and WHY to HOW

This article has focused on what resilience means and why it matters. The next article will move from these principles to a practical engineering approach.

**Engineering Resilience: A Seven-Step Framework for Designing Dependable Systems**

The framework will organize established engineering practices into seven connected steps:

1. Understand the service and its resilience requirements.
2. Identify dependencies and failure domains.
3. Design for redundancy and fault tolerance.
4. Protect data and ensure recoverability.
5. Build capacity and handle unexpected demand.
6. Detect, respond, reconstruct, and recover.
7. Validate, test, and continuously improve.

Within Step 4, data protection will be explored through established approaches such as backups, replication, snapshots, and erasure coding. Erasure coding will serve as a practical storage example, including how data can be distributed and reconstructed across failure domains. We will examine its mathematics, including Reed-Solomon and Locally Repairable Codes, as well as the trade-offs involving storage efficiency, performance, reconstruction, and recovery. It is one part of a broader resilience framework, not a universal answer to every failure scenario.

## Conclusion

Resilience is not about assuming that nothing will fail. Failures are an inevitable part of complex systems. It is about understanding what can fail, preparing for it, and designing systems that can continue operating or recover when they do. **Resilience is not something we add after building a system. It is something we must design into it from the beginning.**

## References and Bibliography

**Latest Events:**
* **[Microsoft 365 Service Disruption (Nov 12–14, 2026)](https://www.365fanatic.com/wp-content/uploads/2026/11/postincidentreport.pdf):** Microsoft. *Preliminary Post-Incident Report for Microsoft 365*. November 15, 2026. Incident IDs EX1550543 / MO1550821.
* **[Microsoft 365 Technical Analysis](https://arstechnica.com/gadgets/2026/11/microsoft-details-how-three-problems-combined-for-a-global-outage/):** Indge, N. "Three Small Failures Combined to Take Down Microsoft 365." *Ars Technica*, November 16, 2026.
* **[FAA Nationwide Ground Stop (Nov 13, 2026)](https://www.faa.gov/newsroom/nationwide-ground-stop-questions-and-answers):** Federal Aviation Administration. *Nationwide Ground Stop: Questions and Answers*. November 15, 2026.
* **[Department of Transportation Update](https://www.transportation.gov/briefing-room/icymi-us-transportation-secretary-sean-p-duffy-announces-lifting-nationwide-ground):** U.S. Department of Transportation. *U.S. Transportation Secretary Sean P. Duffy Announces Lifting of Nationwide Ground Stop, Provides Updates from FAA*. November 13, 2026.
* **[U.S. Banking Outages (Nov 16, 2026)](https://www.reuters.com/legal/transactional/downdetector-reports-outages-major-us-banks-2026-11-16/):** Reuters. "JPMorgan Says Software Bug Slows Its Transactions." November 16, 2026.
* **[U.S. Banking Delays Overview](https://apnews.com/article/aeb4b0d6b6789c8c96bb2520454a6d1e):** Associated Press. "What to Know About the Online Banking Delays That Affected Major US Banks." November 17, 2026.
* **[Anthropic Capacity & Availability Incident (March 2026)](https://www.sec.gov/Archives/edgar/data/2130357/000162828026074338/anthropicpbc-sx1ax3.htm):** Anthropic, PBC. *Amendment No. 3 to Form S-1 Registration Statement*. Filed with the U.S. Securities and Exchange Commission, November 17, 2026.

**Data Center Community & Environmental Context:**
* [Annenberg Public Policy Center, University of Pennsylvania](https://www.annenbergpublicpolicycenter.org/opposition-to-local-data-centers-rises-sharply-annenberg-survey-finds/). "Opposition to Local Data Centers Rises Sharply, Annenberg Survey Finds." August 11, 2026.
* [Pew Research Center](https://www.pewresearch.org/short-reads/2026/09/22/americans-views-of-data-centers-have-turned-more-negative/). "More Americans Now Say Data Centers Are Negative for the Environment, Energy Costs and More." September 22, 2026.

**Systems Resilience & SRE Standards:**
* Ross, R., et al. [*Developing Cyber-Resilient Systems: A Systems Security Engineering Approach to Survivable Systems*](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final). NIST Special Publication 800-160, Volume 2, Revision 1, 2021.
* Beyer, B., Jones, C., Petoff, J., & Murphy, N. R. (Eds.). [*Site Reliability Engineering: How Google Runs Production Systems*](https://sre.google/sre-book/table-of-contents/). O’Reilly Media, 2016.
* International Organization for Standardization. [*ISO 22301:2019: Security and resilience — Business continuity management systems — Requirements*](https://www.iso.org/standard/75106.html).

**Database High Availability & Distributed Storage (Previewed for Article 2):**
* Oracle. [*Introduction to Oracle Real Application Clusters*](https://docs.oracle.com/en/database/oracle/oracle-database/). Oracle Database Documentation.
* Huang, C., Simitci, H., Xu, Y., Ogus, A., Calder, B., Gopalan, P., Li, J., & Yekhanin, S. "[Erasure Coding in Windows Azure Storage](https://www.usenix.org/conference/atc12/technical-sessions/presentation/huang)." *Proceedings of the 2012 USENIX Annual Technical Conference (USENIX ATC 12)*.
* Reed, I. S., & Solomon, G. "[Polynomial Codes Over Certain Finite Fields](https://doi.org/10.1137/0108018)." *Journal of the Society for Industrial and Applied Mathematics*, 1960, 8(2), 300–304.
