# ArmourVault Technologies — Product Catalog

## Company Overview

ArmourVault Technologies is a Boston-based identity-first security company founded in 2010, with a focus on Zero Trust Network Access (ZTNA), Privileged Access Management (PAM), and Identity and Access Management (IAM). ArmourVault serves primarily the financial services, healthcare, and critical infrastructure sectors, with a customer base of 1,800 organizations in 38 countries. The company employs 950 staff, including 300 dedicated to identity threat research.

ArmourVault's founding premise is that the network perimeter is obsolete — every access request must be continuously verified regardless of source. The company's **TrustNone™ Framework** implements the NIST 800-207 Zero Trust Architecture standard and pairs it with behavioral biometrics and risk-based adaptive authentication. ArmourVault is a CVE Numbering Authority (CNA) and regularly publishes security advisories on identity-related vulnerabilities.

Certifications held: SOC 2 Type II, ISO 27001, ISO 27017, FIPS 140-2 Level 3 (cryptographic modules), FedRAMP High (GovCloud), HITRUST CSF, PCI DSS Level 1.

---

## Product Overview: ArmourVault Zero Trust Suite (ZTS)

The **ArmourVault Zero Trust Suite** is a modular, cloud-delivered platform combining ZTNA, PAM, multi-factor authentication (MFA), single sign-on (SSO), and identity governance into a single administrative console. Unlike legacy VPN-dependent architectures, ZTS brokers every connection through ArmourVault's globally distributed proxy network (42 PoPs across 6 continents), ensuring least-privilege access to every application, database, and infrastructure asset.

### Key Differentiators

- **TrustNone™ Continuous Verification**: Re-evaluates risk scores every 90 seconds during active sessions — not just at login.
- **Behavioral Biometrics Engine**: Analyzes typing rhythm, mouse dynamics, and touch patterns to detect account takeover mid-session.
- **Vaultless PAM**: Privileged credentials are ephemeral — generated on demand and rotated immediately after use, eliminating credential stores as attack targets.
- **Universal ZTNA Connector**: Agentless browser-based access for contractors and third parties; full agent for employees on managed devices.
- **Identity Threat Detection & Response (ITDR)**: Dedicated module for detecting Kerberoasting, DCSync, Golden Ticket attacks, and lateral movement.

---

## Solution Tiers

### Tier 1 — Foundation Access

**Ideal for:** Small businesses and startups (5–150 users) needing secure SSO, MFA, and basic access controls without the overhead of enterprise PAM.

**Monthly Pricing:** $6 per user/month  
**Annual Pricing:** $60 per user/year (16.7% discount)  
**Minimum Users:** 5

#### Included Features
- SSO for up to 25 SaaS applications (SAML 2.0, OIDC, OAuth 2.0)
- Adaptive MFA: TOTP, push notification, hardware FIDO2 keys (YubiKey compatible)
- Self-service password reset with identity proofing
- User lifecycle management (provisioning/deprovisioning) via SCIM 2.0
- Basic access request and approval workflows
- Login anomaly detection (geolocation, impossible travel, new device)
- 30-day audit log retention
- Standard SaaS integrations: Google Workspace, Microsoft 365, Salesforce, Slack, Zoom
- Email support (48-hour response SLA)

#### Limitations
- No ZTNA (VPN still required for on-premises resources)
- No PAM capabilities
- Maximum 150 users

---

### Tier 2 — Advanced Zero Trust

**Ideal for:** Mid-market organizations (150–3,000 users) with hybrid environments, remote workforces, and compliance requirements.

**Monthly Pricing:** $16 per user/month  
**Annual Pricing:** $158 per user/year (17.7% discount)  
**Minimum Users:** 50

#### Included Features
Everything in Foundation Access, plus:
- ZTNA for on-premises applications and private cloud resources (replaces VPN)
- Full agent (Windows, macOS, Linux, iOS, Android) + agentless browser access
- ArmourVault Universal Connector: connect any TCP/UDP application in 15 minutes
- 200+ pre-built SaaS connectors
- Role-based access control (RBAC) with attribute-based policies (ABAC)
- Risk-based step-up authentication: elevated risk triggers additional MFA challenges
- Behavioral biometrics monitoring (typing cadence, device posture)
- Device trust enforcement: block unmanaged or non-compliant devices
- Privileged session recording (screen capture + keystroke logging for privileged accounts)
- Lightweight PAM: shared account password management, credential checkout
- Identity governance: access certification campaigns (quarterly)
- 90-day audit log retention
- Integrations: Azure AD, Okta, Duo Security, Cisco ISE, CrowdStrike (device health), ServiceNow
- 24/7 chat and email support with 2-hour response SLA

---

### Tier 3 — Enterprise Zero Trust Command

**Ideal for:** Enterprises, financial institutions, healthcare systems, and government agencies with 3,000+ users requiring full PAM, ITDR, and compliance automation.

**Monthly Pricing:** $28 per user/month  
**Annual Pricing:** $272 per user/year (19% discount)  
**Minimum Users:** 500  
**Volume Discounts:** Tiered discounts at 2,500, 10,000, and 25,000 users

#### Included Features
Everything in Advanced Zero Trust, plus:
- **Vaultless PAM**: Ephemeral credential injection for servers, databases, cloud consoles (no shared passwords)
- Just-In-Time (JIT) access provisioning: privileged access granted for defined time windows only
- Full session recording with OCR-indexed search and anomaly flagging
- **Identity Threat Detection & Response (ITDR)**: Detection of Golden Ticket, Pass-the-Hash, DCSync, Kerberoasting, LDAP reconnaissance
- Threat intelligence integration: MITRE ATT&CK for Enterprise identity-focused TTPs
- Privileged Remote Access (PRA) for third-party vendors with no VPN or agent requirement
- Secrets management: vault for API keys, SSH keys, TLS certificates with automated rotation
- Compliance automation: HIPAA, SOX, PCI DSS, NIST 800-53, FedRAMP, GDPR reporting
- Separation of duties (SoD) conflict detection
- AI-powered access recommendations: flag over-provisioned accounts
- Multi-directory support: Active Directory, Azure AD, LDAP, Ping Identity
- SIEM integration: Splunk, Microsoft Sentinel, IBM QRadar, Sumo Logic
- Dedicated implementation engineer and Customer Success Manager
- 24/7 phone/chat/email support with 30-minute critical SLA
- 365-day audit log retention + immutable archive (7-year for financial compliance)
- Full REST API + Terraform provider for infrastructure-as-code deployment

---

## Technical Specifications

| Specification | Details |
|---|---|
| Global PoP Count | 42 points of presence |
| Connector Latency | <5 ms added latency (P95, nearest PoP) |
| Agent Platforms | Windows 10/11, macOS 12+, Ubuntu/RHEL/CentOS, iOS 15+, Android 12+ |
| Agentless Access | Chromium-based browser extension, any OS |
| Authentication Methods | TOTP, FIDO2/WebAuthn, Push, SMS, Email OTP, Smart Card (PIV/CAC) |
| Directory Sync | AD, Azure AD, LDAP v3, SCIM 2.0, Google Directory |
| Encryption | AES-256-GCM at rest; TLS 1.3 in transit; FIPS 140-2 Level 3 modules |
| Uptime SLA | 99.99% (Enterprise), 99.95% (Advanced) |
| Data Residency | US, EU, UK, CA, AU, JP, SG |

---

## Compliance & Certifications

- SOC 2 Type II (semi-annual audit)
- ISO/IEC 27001:2022 and ISO/IEC 27017
- FIPS 140-2 Level 3 validated cryptographic modules
- FedRAMP High Authorization
- HITRUST CSF v11 Certified
- PCI DSS Level 1 Service Provider
- HIPAA BAA available
- GDPR and UK GDPR compliant

---

## Target Use Cases

1. **VPN Replacement**: ZTNA eliminates broad network access; users reach only the specific applications they're authorized for.
2. **Third-Party Vendor Access**: Agentless privileged remote access with session recording and time-limited credentials for contractors.
3. **Privileged Account Security**: Vaultless PAM eliminates standing admin credentials that attackers target.
4. **Insider Threat Mitigation**: Behavioral biometrics and UEBA flag unusual activity from legitimate accounts.
5. **Merger & Acquisition Integration**: Rapidly federate acquired company identities without full directory migration.
6. **DevOps Secrets Management**: Automated rotation of SSH keys, API tokens, and database passwords integrated with CI/CD pipelines.

---

## Pricing Summary

| Tier | Monthly (per user) | Annual (per user) | Min Users |
|---|---|---|---|
| Foundation Access | $6 | $60 | 5 |
| Advanced Zero Trust | $16 | $158 | 50 |
| Enterprise Zero Trust Command | $28 | $272 | 500 |

*USD pricing. Multi-year contracts (2- and 3-year) available at additional 10–15% discount. Non-profit and education pricing available.*

---

## Contact & Support

- **Sales:** sales@armourvault.com | 1-888-ARMOUR-1
- **Support Portal:** help.armourvault.com
- **Security Advisories:** security.armourvault.com
- **Trust Center:** trust.armourvault.com
