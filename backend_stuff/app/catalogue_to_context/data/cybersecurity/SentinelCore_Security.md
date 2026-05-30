# SentinelCore Security — Product Catalog

## Company Overview

SentinelCore Security is a San Jose-based cybersecurity software vendor founded in 2014, specializing in endpoint detection and response (EDR), extended detection and response (XDR), and Security Information and Event Management (SIEM) solutions for mid-market and enterprise organizations. With over 3,400 enterprise customers across 47 countries and a team of 1,200 security researchers and engineers, SentinelCore has established itself as a recognized leader in AI-driven threat detection. The company holds ISO 27001, SOC 2 Type II, FedRAMP Moderate, and PCI DSS Level 1 certifications.

SentinelCore's core philosophy centers on autonomous threat response — reducing mean time to detect (MTTD) and mean time to respond (MTTR) without requiring constant analyst intervention. The platform ingests over 5 trillion telemetry signals daily and leverages a proprietary behavioral AI engine called **NeuralGuard™** that correlates anomalies across endpoint, network, identity, and cloud data planes.

---

## Product Overview: SentinelCore Unified Defense Platform

The **SentinelCore Unified Defense Platform (UDP)** is a cloud-native, agent-based security suite that consolidates endpoint protection, threat intelligence, SIEM log management, and automated incident response into a single console. It replaces legacy antivirus, standalone firewalls, and siloed SIEM tools with a unified approach to threat visibility.

### Key Differentiators

- **NeuralGuard™ Behavioral AI**: Proprietary ML engine trained on 10+ years of threat data; detects novel malware variants and zero-day exploits with a 99.3% detection rate (independent AV-TEST certification, Q1 2026).
- **1-Click Remediation**: Automated playbooks can isolate endpoints, revoke compromised credentials, and roll back malicious changes within seconds.
- **Unified Console**: Single pane of glass for EDR, XDR, SIEM, vulnerability management, and threat hunting.
- **Threat Intelligence Feed**: Integration with SentinelCore Threat Research Unit (TRU), updated every 15 minutes with IOCs, TTPs, and adversary profiles.
- **Cloud-Native Architecture**: No on-premises hardware required; agent supports Windows, macOS, Linux, iOS, and Android.

---

## Solution Tiers

### Tier 1 — Starter Shield

**Ideal for:** SMBs with 10–200 employees seeking foundational endpoint protection and basic threat visibility.

**Monthly Pricing:** $8 per endpoint/month  
**Annual Pricing:** $84 per endpoint/year (12.5% discount)  
**Minimum Endpoints:** 10

#### Included Features
- Next-generation antivirus (NGAV) with NeuralGuard™ static analysis
- Real-time malware detection and quarantine
- Ransomware behavioral detection and file rollback (up to 72 hours)
- Device firewall and USB device control
- Centralized endpoint inventory dashboard
- Weekly automated threat summary reports
- Email and community forum support (business hours, M–F)
- Windows 10/11 and macOS 13+ support
- 30-day event log retention

#### Limitations
- No EDR telemetry or threat hunting
- No network traffic analysis
- No SIEM integration
- Maximum 200 endpoints

---

### Tier 2 — Professional Defender

**Ideal for:** Growing mid-market companies (200–2,000 employees) with an internal IT security team that needs EDR and incident investigation capabilities.

**Monthly Pricing:** $18 per endpoint/month  
**Annual Pricing:** $185 per endpoint/year (14% discount)  
**Minimum Endpoints:** 50

#### Included Features
Everything in Starter Shield, plus:
- Full EDR telemetry: process trees, file events, network connections, registry changes
- Threat hunting console with pre-built queries (MITRE ATT&CK-mapped)
- Real-time alerts with severity scoring (Critical / High / Medium / Low)
- Automated investigation: root cause analysis timelines
- 1-Click isolation and remediation playbooks
- Vulnerability assessment scanning (agent-based, updated daily)
- Active Directory (Azure AD and on-prem) integration
- SIEM integration via Syslog, CEF, and REST API (Splunk, Microsoft Sentinel, IBM QRadar)
- 90-day event log retention
- Identity threat detection (credential stuffing, pass-the-hash, brute force)
- Mobile device support (iOS 16+, Android 13+)
- 24/7 email and chat support with 4-hour response SLA
- Up to 5 custom detection rules

#### Integrations
Microsoft 365, Google Workspace, Okta, CrowdStrike Falcon X (threat intel), Jira, ServiceNow, Slack, PagerDuty

---

### Tier 3 — Enterprise Command

**Ideal for:** Large enterprises and regulated industries (healthcare, finance, government) with 2,000+ endpoints and dedicated security operations centers (SOCs).

**Monthly Pricing:** $32 per endpoint/month  
**Annual Pricing:** $320 per endpoint/year (16.7% discount)  
**Minimum Endpoints:** 500  
**Volume Discounts:** Available for 5,000+ endpoints (contact sales)

#### Included Features
Everything in Professional Defender, plus:
- Full XDR: cross-domain correlation across endpoint, network, cloud, and identity
- Cloud workload protection (AWS EC2, Azure VMs, GCP Compute — agentless option available)
- Network Detection and Response (NDR) via sensor deployment or cloud traffic mirroring
- SIEM-as-a-Service with SentinelCore Nexus SIEM: unlimited log ingestion, 1-year retention
- AI-powered SOAR (Security Orchestration, Automation, and Response): 150+ pre-built playbooks
- Managed Threat Hunting (MTH): SentinelCore analysts perform proactive hunts monthly
- Executive risk dashboard with board-ready reporting
- Compliance reporting packs: HIPAA, PCI DSS, NIST 800-53, SOC 2, ISO 27001, CIS Controls
- Custom YARA and Sigma rule deployment
- Multi-tenant management for MSSPs and enterprise subsidiaries
- Dedicated Customer Success Manager and TAM (Technical Account Manager)
- 24/7 phone, email, and chat support with 1-hour critical response SLA
- 365-day event log retention + cold storage archive option (5-year)
- API access for full platform automation
- Up to 500 custom detection rules

#### Integrations (Additional)
Palo Alto Cortex XSOAR, AWS Security Hub, Azure Security Center, Google Chronicle, Tenable.io, Qualys, Cisco Umbrella, Zscaler, Sailpoint IIQ, CyberArk PAM

---

## Technical Specifications

| Specification | Details |
|---|---|
| Agent Size | 42 MB (Windows), 38 MB (macOS), 28 MB (Linux) |
| CPU Overhead | <1% average; <3% peak during scans |
| Memory Footprint | 120–180 MB RAM |
| Network Bandwidth | ~15 KB/s telemetry (steady state) |
| Deployment Methods | MSI/PKG installer, GPO, SCCM/Intune, Ansible, Chef, Puppet, Terraform |
| Data Residency | US, EU (Frankfurt), AU (Sydney), Singapore |
| Uptime SLA | 99.95% (Enterprise), 99.9% (Professional) |
| API | RESTful JSON API; OpenAPI 3.0 spec published |

---

## Compliance & Certifications

- ISO/IEC 27001:2022 certified
- SOC 2 Type II (annual audit)
- FedRAMP Moderate Authorization (GovCloud environment)
- PCI DSS Level 1 Service Provider
- GDPR compliant (EU-US Data Privacy Framework)
- HIPAA Business Associate Agreement available

---

## Target Use Cases

1. **Ransomware Prevention**: Behavioral AI detects encryption behavior before files are locked; rollback restores affected files automatically.
2. **Insider Threat Detection**: UEBA (User and Entity Behavior Analytics) flags anomalous data exfiltration or privilege escalation.
3. **Supply Chain Attack Defense**: Software bill of materials (SBOM) tracking detects compromised third-party libraries.
4. **Zero-Day Exploit Blocking**: Memory protection and process injection detection stop fileless attacks before signature updates.
5. **SOC Efficiency**: SOAR automation reduces analyst alert fatigue by auto-closing 68% of low-fidelity alerts.

---

## Pricing Summary

| Tier | Monthly (per endpoint) | Annual (per endpoint) | Min Endpoints |
|---|---|---|---|
| Starter Shield | $8 | $84 | 10 |
| Professional Defender | $18 | $185 | 50 |
| Enterprise Command | $32 | $320 | 500 |

*All pricing in USD. Prices listed are list rate; volume and multi-year discounts available. Free 30-day trial available for Starter and Professional tiers.*

---

## Contact & Support

- **Sales:** sales@sentinelcore.io | 1-800-SENTINEL
- **Support Portal:** support.sentinelcore.io
- **Documentation:** docs.sentinelcore.io
- **Status Page:** status.sentinelcore.io
