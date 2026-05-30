# NetFortress Systems — Product Catalog

## Company Overview

NetFortress Systems is a Dallas, Texas-based cybersecurity company founded in 2007, specializing in network security, next-generation firewall (NGFW) technology, and Security Operations Center (SOC)-as-a-service offerings. Originally built on hardware firewall appliances, NetFortress pivoted to cloud-delivered security in 2018 with the launch of its SASE (Secure Access Service Edge) platform. Today, the company serves 6,200 customers globally, with particular strength in the manufacturing, retail, and logistics verticals.

NetFortress employs 2,100 people across 14 offices worldwide, including a 24/7 managed SOC staffed by 400 security analysts in Austin, Dublin, and Singapore. The company is publicly traded (NASDAQ: NFSY) and reported $480M in annual recurring revenue in FY2025.

Certifications: ISO 27001, SOC 2 Type II, PCI DSS Level 1, NERC CIP (energy sector), Common Criteria EAL4+.

---

## Product Overview: NetFortress CloudShield SASE

The **NetFortress CloudShield SASE Platform** converges network security and wide-area networking (WAN) into a cloud-delivered service. It combines Secure Web Gateway (SWG), Cloud Access Security Broker (CASB), ZTNA, SD-WAN, DNS-layer security, and next-generation firewall-as-a-service (FWaaS) under a single management console — NetFortress Command Center.

### Key Differentiators

- **Unified SASE Architecture**: Single vendor, single console, single policy engine — no stitching together multiple products.
- **ThreatSense IQ**: Real-time threat intelligence engine correlating 12 billion daily DNS queries, web transactions, and network flows.
- **Inline CASB**: Full traffic inspection for 35,000+ SaaS applications including DLP policy enforcement without agents.
- **BranchConnect SD-WAN**: Zero-touch provisioning deploys branch office connectivity in under 2 hours.
- **Managed SOC Integration**: Native connection to NetFortress's 24/7 SOC for organizations that want managed detection and response (MDR) on top of the platform.

---

## Solution Tiers

### Tier 1 — CloudShield Essentials

**Ideal for:** Small to mid-sized businesses (25–500 users) that need secure internet access and basic SaaS controls without full SASE complexity.

**Monthly Pricing:** $9 per user/month  
**Annual Pricing:** $95 per user/year (11.9% discount)  
**Minimum Users:** 25

#### Included Features
- DNS-layer security: block malware, phishing, botnet C2 domains (powered by ThreatSense IQ)
- Secure Web Gateway (SWG): URL filtering across 83 content categories
- SSL/TLS traffic inspection (certificate-based)
- Basic cloud application visibility (shadow IT discovery for top 5,000 apps)
- Acceptable use policy enforcement
- User-based reporting and activity logs
- 60-day log retention
- Multi-site support (up to 5 office locations)
- Roaming client for remote users (Windows/macOS)
- Email support and knowledge base access (business hours)

#### Limitations
- No CASB policy enforcement (visibility only)
- No ZTNA (no private application access)
- No SD-WAN capabilities
- No DLP

---

### Tier 2 — CloudShield Advanced

**Ideal for:** Mid-market companies (500–5,000 users) with distributed workforces, cloud-heavy environments, and data protection requirements.

**Monthly Pricing:** $21 per user/month  
**Annual Pricing:** $210 per user/year (16.7% discount)  
**Minimum Users:** 100

#### Included Features
Everything in CloudShield Essentials, plus:
- **Inline CASB**: Enforce access policies on 35,000+ SaaS apps (block, allow, read-only, DLP)
- **Data Loss Prevention (DLP)**: 150+ pre-built data classifiers (PII, PHI, PCI, source code, financial data); custom regex patterns
- Cloud app risk scoring and sanctioned/unsanctioned app management
- ZTNA: Agentless and agent-based private application access (replaces remote access VPN)
- Remote Browser Isolation (RBI): Execute risky web content in cloud sandbox — never reaches endpoint
- Firewall-as-a-Service (FWaaS): Layer 7 policy enforcement, IPS/IDS, application-aware rules
- Advanced threat protection: sandboxed file analysis (PDF, Office, executables) with <60-second verdict
- 180-day log retention
- SIEM integration: Syslog/CEF export to Splunk, Sentinel, QRadar, Sumo Logic
- API integrations: Okta, Azure AD, CrowdStrike, Carbon Black
- 24/7 chat and email support with 4-hour SLA

---

### Tier 3 — CloudShield Enterprise SASE

**Ideal for:** Large enterprises, MSSPs, and organizations in regulated industries needing full SASE convergence, SD-WAN, and optional managed SOC services.

**Monthly Pricing:** $38 per user/month  
**Annual Pricing:** $370 per user/year (18.9% discount)  
**Minimum Users:** 500

**SD-WAN Add-On (Branch Connectivity):** $200/site/month (includes BranchConnect appliance hardware lease)

#### Included Features
Everything in CloudShield Advanced, plus:
- **BranchConnect SD-WAN**: Application-aware traffic steering, WAN optimization, dual ISP failover
- Zero-touch provisioning for branch appliances (NetFortress CB-3000 and CB-5000 series)
- Multi-cloud connectivity: direct integration to AWS Transit Gateway, Azure Virtual WAN, Google Cloud Network Connectivity Center
- **NetFortress MDR (Managed Detection and Response)**: 24/7 SOC monitoring, alert triage, incident escalation, monthly threat reports
- UEBA: User and entity behavioral analytics for insider threat and compromised account detection
- Deception technology: honey tokens and honey credentials that trigger high-fidelity alerts
- Advanced DLP: endpoint DLP agent, email DLP (Microsoft 365, Google Workspace), print/USB controls
- Compliance reporting: PCI DSS, HIPAA, GDPR, NIST CSF, ISO 27001, CIS Benchmark
- Executive dashboard with risk scoring by business unit
- Dedicated implementation team and TAM
- 99.999% SLA on DNS and SWG services
- 365-day log retention + cold archive (3-year)
- Full REST API; Terraform and Ansible integrations
- Multi-tenant console for MSSP partners with white-label option

#### MDR Tiers (Optional Add-Ons)
| MDR Level | Features | Monthly Cost |
|---|---|---|
| MDR Essentials | 8×5 SOC monitoring, alert triage | +$4/user/month |
| MDR Standard | 24×7 SOC, incident response, monthly report | +$10/user/month |
| MDR Elite | 24×7 SOC + dedicated analyst team, proactive threat hunting | +$22/user/month |

---

## Technical Specifications

| Specification | Details |
|---|---|
| Global PoP Locations | 58 cities across North America, Europe, Asia-Pacific, Middle East |
| DNS Query Processing | 12 billion queries/day |
| Throughput (FWaaS) | Up to 100 Gbps per PoP cluster |
| SWG Latency | <10 ms added (P99 at nearest PoP) |
| File Sandbox Verdict Time | <60 seconds (99th percentile) |
| Client OS Support | Windows 10/11, macOS 12+, iOS 15+, Android 12+, ChromeOS |
| SD-WAN Appliances | CB-1000 (50 users), CB-3000 (250 users), CB-5000 (1,000 users) |
| Deployment | Cloud SaaS + lightweight roaming client; on-prem connector for legacy apps |
| Log Formats | CEF, LEEF, JSON; native connectors for Splunk, Sentinel, QRadar |

---

## Compliance & Certifications

- ISO/IEC 27001:2022
- SOC 2 Type II
- PCI DSS Level 1 Service Provider
- NERC CIP (applicable to energy and utilities customers)
- Common Criteria EAL4+ (BranchConnect appliances)
- GDPR compliant; EU-US DPF certified
- HIPAA BAA available

---

## Target Use Cases

1. **Hybrid Workforce Security**: Consistent policy enforcement whether employees are in-office, remote, or on mobile — without backhauling traffic through a data center.
2. **Shadow IT Governance**: Discover and control unsanctioned SaaS adoption; enforce DLP policies on personal cloud storage use.
3. **Retail PCI Compliance**: Segment point-of-sale networks, enforce payment application policies, and generate automated PCI DSS audit reports.
4. **Manufacturing OT/IT Convergence**: Extend ZTNA and firewall policies to operational technology (OT) environments without disrupting production systems.
5. **Branch Office Modernization**: Replace expensive MPLS circuits with SD-WAN over broadband, reducing WAN costs by an average of 47%.

---

## Pricing Summary

| Tier | Monthly (per user) | Annual (per user) | Min Users |
|---|---|---|---|
| CloudShield Essentials | $9 | $95 | 25 |
| CloudShield Advanced | $21 | $210 | 100 |
| CloudShield Enterprise SASE | $38 | $370 | 500 |

*Prices in USD. SD-WAN hardware add-on billed separately. MDR services available as add-ons to Enterprise tier.*

---

## Contact & Support

- **Sales:** enterprise@netfortress.com | 1-877-NETFORT
- **Partner Portal:** partners.netfortress.com
- **24/7 SOC Hotline:** 1-877-NETFORT (Option 3)
- **Documentation:** docs.netfortress.com
