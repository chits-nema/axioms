# NimbusVault Cloud — Product Catalog

## Company Overview

NimbusVault Cloud is a Seattle-based cloud storage and content collaboration company founded in 2011. Built from the ground up for enterprise IT, NimbusVault differentiates itself from consumer-grade file sync tools by prioritizing data sovereignty, granular permissions, and enterprise governance. The company serves 9,200 organizations worldwide, from 50-person law firms to Fortune 500 enterprises, spanning legal, healthcare, financial services, and government sectors.

NimbusVault employs 1,800 people, operates its own multi-region private cloud infrastructure (not resold AWS/Azure), and reported $340M in ARR in FY2025. The company has raised $780M in total funding and is considering an IPO in 2026. NimbusVault processes 14 petabytes of data transfers per day across its six global data centers (Virginia, Oregon, Frankfurt, London, Singapore, Sydney).

Certifications: SOC 2 Type II, ISO 27001, ISO 27017, ISO 27018, FedRAMP High, HIPAA, PCI DSS Level 1, DoD IL4 (Impact Level 4).

---

## Product Overview: NimbusVault Enterprise Content Cloud

The **NimbusVault Enterprise Content Cloud** is a unified platform for secure file storage, synchronization, collaboration, and content lifecycle management. It addresses a fundamental enterprise tension: enabling frictionless collaboration while enforcing strict data governance, retention policies, and compliance controls.

### Key Differentiators

- **Zero-Knowledge Encryption Option**: Enterprises can deploy customer-managed encryption keys (CMEK) via their own AWS KMS, Azure Key Vault, or HashiCorp Vault — NimbusVault never sees plaintext data.
- **Content Shield DLP**: Built-in Data Loss Prevention automatically scans uploads and shares for PII, PHI, trade secrets, and source code; blocks or watermarks policy-violating content.
- **Intelligent Content Lifecycle**: AI-powered tagging, retention schedules, and legal hold management — content is automatically classified, retained per policy, and disposed of on schedule.
- **Hybrid Deployment Option**: NimbusVault Edge appliance allows on-premises caching for high-bandwidth workflows (video production, CAD/engineering) with cloud tiering.
- **Federated Identity**: Deep integration with every major enterprise IdP — no shadow IT accounts; every user is provisioned and deprovisioned through HR systems.

---

## Solution Tiers

### Tier 1 — NimbusVault Business

**Ideal for:** Small to mid-sized teams (5–300 users) needing secure, centralized cloud storage with robust sharing controls and a professional collaboration experience.

**Monthly Pricing:** $12 per user/month  
**Annual Pricing:** $120 per user/year (16.7% discount)  
**Storage:** 2 TB shared pool per team (expandable at $0.025/GB/month)  
**Minimum Users:** 5

#### Included Features
- Unlimited file size uploads (individual file limit: 50 GB)
- File versioning: 180-day version history
- Granular folder and file permissions (View, Edit, Upload, Download, Co-owner)
- Secure external sharing with expiry dates, password protection, and download limits
- Desktop sync client (Windows, macOS)
- Mobile apps (iOS, Android) with offline access
- Web interface with in-browser preview for 120+ file types
- Microsoft Office Online and Google Docs integration (co-edit Office files in browser)
- Basic content search (filename, metadata)
- Two-factor authentication enforcement
- 99.9% uptime SLA
- Email support (business hours, 24-hour SLA)

---

### Tier 2 — NimbusVault Professional

**Ideal for:** Growing companies (300–3,000 users) in regulated industries needing advanced security controls, compliance features, and enterprise integrations.

**Monthly Pricing:** $22 per user/month  
**Annual Pricing:** $216 per user/year (18% discount)  
**Storage:** Unlimited (subject to fair use; throttling above 1 PB per org)  
**Minimum Users:** 50

#### Included Features
Everything in NimbusVault Business, plus:
- Unlimited storage (no per-user caps)
- File versioning: unlimited version history
- **Content Shield DLP**: Automated scanning for 200+ sensitive data types; block, quarantine, or watermark on policy violation
- Advanced content search: full-text search within documents, spreadsheets, PDFs, and images (OCR)
- **eSignature Integration**: Built-in e-signature workflows (powered by DocuSign and Adobe Acrobat Sign)
- Watermarking: dynamic visual watermarks with viewer identity on shared documents
- Metadata templates and custom metadata fields for document classification
- Retention policies: set automated deletion or archive schedules by folder, file type, or metadata
- Legal hold: freeze specific content from deletion during litigation
- Single Sign-On (SSO): SAML 2.0 and OIDC integration with Okta, Azure AD, Google, Ping
- SCIM 2.0 user provisioning from Okta, Azure AD, Workday
- Audit logging: all user actions logged with 365-day retention
- SIEM integration: export logs to Splunk, Microsoft Sentinel, Sumo Logic, Datadog
- 99.95% uptime SLA
- Dedicated account manager
- 24/7 chat and email support with 4-hour SLA

#### Key Integrations
Salesforce, Microsoft Teams, Slack, Zoom, Jira, Confluence, SharePoint, DocuSign, Adobe Sign, Workday

---

### Tier 3 — NimbusVault Enterprise Sovereign

**Ideal for:** Large enterprises, government agencies, healthcare systems, law firms, and financial institutions with complex compliance, data sovereignty, and hybrid infrastructure requirements.

**Monthly Pricing:** Custom (starting at $32 per user/month for standard configuration)  
**Annual Pricing:** Custom; multi-year discounts available  
**Storage:** Unlimited  
**Minimum Users:** 500

#### Included Features
Everything in NimbusVault Professional, plus:
- **Zero-Knowledge Encryption (CMEK)**: Customer manages encryption keys; NimbusVault cannot access content. Supports AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault.
- **NimbusVault Edge Appliance**: On-premises caching and local LAN sync for high-throughput workflows; models NV-2000 (100 TB), NV-5000 (500 TB), NV-10000 (1 PB).
- **Intelligent Content Lifecycle Manager**: AI-powered content classification, automated retention schedule enforcement, and chain-of-custody documentation for legal admissibility.
- **Advanced Governance Console**: Centralized policy management across subsidiaries, regions, and departments with role-based admin delegation.
- Multi-geo data residency: choose which regions store your data; real-time replication controls.
- **Federated Content Search**: Search across all connected content repositories including Microsoft SharePoint, Box, Dropbox, and on-premises file servers from one interface.
- External collaboration workspace: invite vendors, clients, and partners to secure shared spaces with fine-grained permission isolation.
- Content Classification Labels: Microsoft Purview Information Protection (MIP) label compatibility.
- In-place holds and GDPR right-to-erasure automation.
- Custom branded upload portals: allow external parties to securely deliver files to your organization.
- Dedicated private cloud tenant option (single-tenant infrastructure, dedicated hardware).
- SLA: 99.99% uptime with financial penalties.
- 24/7 phone, chat, and email support with 30-minute critical response SLA.
- Dedicated implementation team, CSM, and TAM.
- Full REST API, SDK (Python, Java, Node.js, .NET), Webhook events.

---

## Technical Specifications

| Specification | Details |
|---|---|
| Data Centers | Virginia (US-East), Oregon (US-West), Frankfurt (EU), London (UK), Singapore (AP), Sydney (AU) |
| Encryption at Rest | AES-256 (platform-managed or customer-managed keys) |
| Encryption in Transit | TLS 1.3 |
| Maximum File Size | 150 GB (Business), 500 GB (Professional), Unlimited (Enterprise) |
| Sync Client OS | Windows 10/11, macOS 11+, Ubuntu 20.04+ |
| Mobile OS | iOS 15+, Android 12+ |
| API | RESTful JSON; SDKs for Python, Java, Node.js, .NET, PHP, Ruby |
| Directory Sync | SCIM 2.0; Okta, Azure AD, Google Directory, Ping, OneLogin |
| Offline Access | Full offline sync on desktop and mobile |
| CDN | Akamai CDN for file delivery acceleration globally |

---

## Compliance & Certifications

- SOC 2 Type II (annual audit)
- ISO/IEC 27001:2022, ISO 27017, ISO 27018
- FedRAMP High (US GovCloud environment)
- HIPAA BAA available (Professional and Enterprise)
- PCI DSS Level 1 Service Provider
- DoD Impact Level 4 (IL4)
- GDPR; UK GDPR; PIPL (China) data transfer compliant
- CJIS compliant (law enforcement sector)

---

## Target Use Cases

1. **Legal Document Management**: Law firms store case files with granular access controls, legal holds, and court-admissible audit trails.
2. **Healthcare Clinical Records Collaboration**: HIPAA-compliant secure sharing of radiology images, pathology reports, and case notes between providers.
3. **Engineering/CAD File Sync**: NimbusVault Edge appliance provides local LAN-speed access for large CAD and BIM files with cloud backup.
4. **Government Content Management**: FedRAMP High and IL4 authorization for federal agency document management and inter-agency collaboration.
5. **M&A Due Diligence Rooms**: Secure virtual data rooms with granular permission controls and complete access audit logs for deal teams.

---

## Pricing Summary

| Tier | Monthly (per user) | Annual (per user) | Storage |
|---|---|---|---|
| NimbusVault Business | $12 | $120 | 2 TB shared pool |
| NimbusVault Professional | $22 | $216 | Unlimited |
| NimbusVault Enterprise Sovereign | From $32 | Custom | Unlimited + Edge |

*USD pricing. Hardware appliance (Edge) priced separately. GovCloud environment available for Enterprise.*

---

## Contact & Support

- **Sales:** enterprise@nimbusvault.com | 1-866-NIMBUS-1
- **Partner Program:** partners.nimbusvault.com
- **Trust & Compliance:** trust.nimbusvault.com
- **Developer Portal:** dev.nimbusvault.com
