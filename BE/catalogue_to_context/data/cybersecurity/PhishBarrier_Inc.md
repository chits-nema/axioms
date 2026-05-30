# PhishBarrier Inc. — Product Catalog

## Company Overview

PhishBarrier Inc. is an Austin, Texas-based email and human risk security company founded in 2018. The company was built on the premise that 91% of cyberattacks begin with a phishing email, yet most organizations invest disproportionately in perimeter defenses while neglecting the human attack surface. PhishBarrier delivers AI-powered email security, automated security awareness training (SAT), and human risk scoring that together transform employees from the weakest link into an active line of defense.

PhishBarrier has grown to 580 employees and serves 4,100 customers across 62 countries, with particular strength in the education, non-profit, healthcare, and SMB sectors. The company processed 28 billion emails in 2025, blocking 99.7% of phishing, BEC (Business Email Compromise), and malware-laden emails. PhishBarrier received the 2025 SE Labs AAA Rating for Email Security and is rated as a Customers' Choice in the 2026 Gartner Peer Insights Voice of the Customer report for Email Security.

Certifications: SOC 2 Type II, ISO 27001, FERPA compliant (education sector), CIPA compliant.

---

## Product Overview: PhishBarrier Human Defense Platform

The **PhishBarrier Human Defense Platform** integrates two mutually reinforcing systems: an AI-powered email security gateway and a behavioral security awareness training engine. Unlike standalone email filters or generic compliance training tools, PhishBarrier continuously feeds real-world threat intelligence from email telemetry directly into personalized training simulations, creating a closed feedback loop that measurably reduces human risk over time.

### Key Differentiators

- **Adaptive AI Email Filter**: Uses transformer-based NLP models to detect novel BEC, spear phishing, and vendor impersonation attacks that bypass traditional reputation-based filters. Trained on 500M+ historical phishing samples.
- **HumanRisk Score™**: A dynamic per-employee risk score (0–100) updated in real-time based on phishing simulation performance, training completion, actual click behavior, and department peer benchmarking.
- **Simulation-to-Training Pipeline**: When an employee clicks a simulated phish, they are immediately enrolled in a targeted 3-minute micro-learning module relevant to the specific attack type.
- **Threat Nudges**: In-email warning banners that appear in real-time for suspicious-but-not-blocked emails, allowing employees to make informed decisions.
- **Vendor/Supply Chain Email Fraud Detection**: Detects lookalike domains, domain spoofing, and reply-to manipulation targeting accounts payable and procurement.

---

## Solution Tiers

### Tier 1 — PhishBarrier Guard

**Ideal for:** Small organizations (10–250 users) seeking reliable email protection and foundational security awareness training without complex configuration.

**Monthly Pricing:** $4 per user/month  
**Annual Pricing:** $40 per user/year (16.7% discount)  
**Minimum Users:** 10

#### Included Features

**Email Security:**
- AI-powered anti-phishing and anti-malware gateway
- Spam filtering with 99.9% accuracy (false positive rate <0.01%)
- Attachment sandboxing for Office documents, PDFs, and executables
- URL rewriting and time-of-click URL re-evaluation
- SPF, DKIM, DMARC enforcement and monitoring
- Basic BEC protection: display name spoofing and domain lookalike detection

**Security Awareness Training:**
- Access to 180+ pre-built training modules (5–15 minutes each) covering phishing, passwords, social engineering, physical security
- 12 monthly phishing simulation templates
- Automated simulation campaigns (set-it-and-forget-it scheduling)
- Training completion tracking and certificate generation
- HumanRisk Score™ dashboard (department-level view)

**Support:** Email support, knowledge base, video tutorials (business hours)

#### Compatible Email Platforms
Microsoft 365, Google Workspace (gateway mode or API inline mode)

---

### Tier 2 — PhishBarrier Pro Shield

**Ideal for:** Mid-sized organizations (250–2,500 users) requiring advanced threat protection, detailed human risk analytics, and compliance-mapped training curricula.

**Monthly Pricing:** $9 per user/month  
**Annual Pricing:** $88 per user/year (18.5% discount)  
**Minimum Users:** 50

#### Included Features

Everything in PhishBarrier Guard, plus:

**Email Security:**
- Advanced BEC protection: financial wire fraud patterns, CFO/CEO impersonation, multi-signal vendor fraud detection
- QR code phishing detection (quishing)
- Voice phishing (vishing) awareness integration with mobile alerting
- Internal email threat detection (compromised internal accounts spreading malware)
- DMARC aggregate and forensic reporting dashboard
- Email quarantine management with one-click release
- Threat intelligence sharing with other PhishBarrier customers (opt-in)
- 90-day email threat log retention

**Security Awareness Training:**
- 600+ training modules including video, interactive, and gamified formats
- Compliance training packs: HIPAA, PCI DSS, GDPR, FERPA, SOX, CCPA (mapped to regulatory requirements)
- Customizable training paths by department, role, and risk score
- HumanRisk Score™ per individual employee with trend graphs
- Automated remediation training triggered by simulation failures
- Phishing simulation templates: 1,500+ templates across 12 attack categories (spear phish, vishing, SMS/smishing, QR code)
- Department benchmarking: compare phish-click rates to industry peers
- Manager reporting portal: line managers see their team's risk scores
- 24/7 chat and email support with 2-hour SLA

---

### Tier 3 — PhishBarrier Enterprise Fortress

**Ideal for:** Large enterprises, universities, healthcare systems, and financial institutions (2,500+ users) with sophisticated threat environments, regulatory compliance mandates, and enterprise reporting needs.

**Monthly Pricing:** $16 per user/month  
**Annual Pricing:** $152 per user/year (20.8% discount)  
**Minimum Users:** 500

#### Included Features

Everything in PhishBarrier Pro Shield, plus:

**Email Security:**
- Account Takeover (ATO) Protection: detects compromised Microsoft 365 and Google Workspace accounts via login anomalies and email behavior changes
- Malicious OAuth app detection: flag unauthorized third-party app authorizations
- Email data loss prevention (DLP): block outbound emails containing SSNs, credit card numbers, PHI, proprietary source code
- Encrypted email delivery: S/MIME and TLS enforcement policies
- Advanced threat investigation console: full email header analysis, attachment forensics, URL detonation reports
- Threat response automation: auto-remediate malicious emails from all user inboxes across organization (mass delete)
- 365-day email threat log retention + immutable archive

**Security Awareness Training:**
- Unlimited training module library (900+ modules, updated monthly)
- AI-personalized learning paths: automatically assign modules based on individual HumanRisk Score™ and demonstrated weaknesses
- Culture survey tool: measure security culture across business units using validated assessment framework
- Board and executive reporting: present human risk posture with benchmarking against Fortune 500 peers
- Physical security simulation: tailgating, vishing, and USB drop test coordination tools
- Multilingual training: 35 languages supported
- LMS integration: push training completion data to Workday Learning, Cornerstone, SAP SuccessFactors, Docebo
- API access for HR system integration (Workday, ADP, BambooHR) for automated user provisioning

**Support & Services:**
- Dedicated Customer Success Manager
- Quarterly human risk review with PhishBarrier security advisor
- 24/7 phone, chat, and email support with 1-hour critical SLA
- Custom phishing template creation service (10 custom templates/year included)
- SIEM integration: Splunk, Microsoft Sentinel, Sumo Logic (threat event forwarding)

---

## Technical Specifications

| Specification | Details |
|---|---|
| Email Processing Speed | Average 2.3-second delivery (including scanning) |
| Detection Rate | 99.7% phishing/BEC/malware detection (SE Labs AAA certified) |
| False Positive Rate | <0.01% |
| Deployment Mode | MX Record (gateway), API inline (Microsoft 365/Google), journaling |
| Training Module Formats | Video (HD), SCORM 1.2/2004, xAPI/TinCan, interactive HTML5 |
| Simulation Campaign Features | Smart scheduling (avoid weekends/holidays), timezone-aware delivery |
| SIEM Export Formats | CEF, JSON, Syslog |
| API | RESTful; Swagger documentation; webhook support |
| Data Residency | US, EU (Ireland), CA, AU |

---

## Compliance & Certifications

- SOC 2 Type II
- ISO/IEC 27001:2022
- FERPA compliant (student data protection)
- CIPA compliant (K-12 filtering)
- GDPR compliant (EU-US DPF)
- HIPAA BAA available
- CCPA compliant

---

## Target Use Cases

1. **Phishing & BEC Prevention**: Block sophisticated spear phishing and business email compromise before they reach employee inboxes.
2. **Compliance Training Automation**: Automate annual security awareness training and maintain audit-ready completion records for HIPAA, PCI DSS, and SOX.
3. **Human Risk Reduction Program**: Run a measurable security culture improvement initiative; most customers reduce phish-click rates by 76% within 12 months.
4. **Account Takeover Detection**: Identify when a Microsoft 365 or Google Workspace account has been compromised and auto-remediate.
5. **Higher Education Security**: Protect universities with large, rotating user populations (students, faculty, staff) and FERPA compliance requirements.

---

## Pricing Summary

| Tier | Monthly (per user) | Annual (per user) | Min Users |
|---|---|---|---|
| PhishBarrier Guard | $4 | $40 | 10 |
| PhishBarrier Pro Shield | $9 | $88 | 50 |
| PhishBarrier Enterprise Fortress | $16 | $152 | 500 |

*USD pricing. Education and non-profit pricing available at 20% discount. Free 30-day trial (up to 100 users). Volume pricing for 10,000+ users.*

---

## Contact & Support

- **Sales:** sales@phishbarrier.com | 1-844-PHISH-00
- **Partner Program:** partners.phishbarrier.com
- **Threat Blog:** blog.phishbarrier.com
- **Support:** help.phishbarrier.com
