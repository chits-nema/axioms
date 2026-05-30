# ClearDrive Collaboration — Product Catalog

## Company Overview

ClearDrive Collaboration is a Toronto-based cloud content management and secure file sharing company founded in 2013. ClearDrive positions itself as the compliance-first alternative to generic file sync tools, with a particular emphasis on serving professional services firms, accounting practices, law firms, and consultancies where client confidentiality is non-negotiable.

ClearDrive serves 18,000 organizations — predominantly SMBs and mid-market firms — in over 90 countries. The company has 380 employees and reported $115M in ARR in FY2025. ClearDrive's focus on simplicity and client portal functionality has made it a preferred tool for client-facing document workflows: firms can share deliverables, collect documents from clients, and obtain e-signatures without requiring clients to create an account or install software.

Certifications: SOC 2 Type II, ISO 27001, PIPEDA compliant (Canada), GDPR, HIPAA BAA available.

---

## Product Overview: ClearDrive Secure Workspace

The **ClearDrive Secure Workspace** is a cloud content management platform combining internal team storage, external client portals, and automated document workflows. Its core design principle is that file sharing with external parties — clients, auditors, regulators, counterparties — should be as secure as internal storage without requiring the external party to adopt new software.

### Key Differentiators

- **Client Portal Engine**: Create branded, password-free secure portals for each client with drag-and-drop document collection, status tracking, and automated deadline reminders.
- **Dynamic Watermarking**: All documents shared externally are automatically watermarked with the recipient's name, email, IP address, and timestamp — dynamically rendered so screenshots are traceable.
- **Auto-Expiry Links**: Every external share link automatically expires (configurable 1–365 days); download and view counts are logged in real-time.
- **Checklist Automation**: Define document intake checklists; clients see exactly which documents are still needed; automated reminders reduce follow-up overhead.
- **No-Account Client Access**: External clients view and upload documents via secure link — no ClearDrive account required. For regulated industries, identity-proofed access with SMS OTP or government ID verification is available.

---

## Solution Tiers

### Tier 1 — ClearDrive Starter

**Ideal for:** Independent professionals, small firms (1–10 users) needing simple, secure cloud storage and basic client document collection.

**Monthly Pricing:** $10 per user/month  
**Annual Pricing:** $96 per user/year (20% discount)  
**Storage:** 1 TB per user  
**Minimum Users:** 1

#### Included Features
- Unlimited file uploads (maximum 5 GB per file)
- File versioning (30-day history)
- Secure external file sharing with link expiry and password protection
- View/download analytics per shared link
- **Client Portal (basic)**: Up to 10 active client portals simultaneously
- Document request checklists (up to 5 items per checklist)
- Auto-reminders (email) for outstanding documents
- Dynamic watermarking on shared documents
- Desktop sync (Windows, macOS) + mobile apps (iOS, Android)
- In-browser document preview (100+ file types)
- 2FA enforcement
- 30-day audit log
- Email support (business hours, 48-hour SLA)

#### Supported File Preview Types
PDF, Word (.docx/.doc), Excel (.xlsx/.xls), PowerPoint (.pptx/.ppt), Images (JPEG, PNG, TIFF, HEIC), Video (MP4, MOV up to 2 GB), AutoCAD (.dwg basic), ZIP (index view)

---

### Tier 2 — ClearDrive Professional

**Ideal for:** Professional services firms (10–200 users) — accounting practices, law firms, consultancies, financial advisors — that manage ongoing client relationships and need advanced portal and workflow features.

**Monthly Pricing:** $22 per user/month  
**Annual Pricing:** $208 per user/year (21.2% discount)  
**Storage:** Unlimited  
**Minimum Users:** 5

#### Included Features
Everything in ClearDrive Starter, plus:
- Unlimited active client portals
- **Branded Client Portal**: Custom subdomain (yourfirm.cleardrive.com), logo, color scheme, custom welcome message
- Document request checklists with unlimited items; conditional logic (if Document A approved, request Document B)
- Automated escalation workflows: auto-escalate overdue requests to senior contact after N days
- **e-Signature Integration**: Native ClearDrive e-sign (unlimited signatures); integrations with DocuSign and Adobe Acrobat Sign
- **ClearDrive Forms**: Create secure intake forms for client onboarding; responses stored as structured data + attached documents
- Identity-proofed client access (SMS OTP verification before viewing portal)
- Bulk client portal creation via CSV import
- Document approval workflows: internal review and approval before sharing with client
- Advanced access controls: per-folder permissions, time-limited access, IP allowlisting for sensitive portals
- Retention policies and scheduled deletion
- Full-text search within documents (OCR enabled)
- SIEM-compatible audit log export (JSON) with 365-day retention
- Integrations: Microsoft 365, Google Workspace, Salesforce, HubSpot, Clio (legal practice management), QuickBooks, Xero
- 24/7 chat and email support with 2-hour SLA

---

### Tier 3 — ClearDrive Enterprise

**Ideal for:** Large professional services networks, financial institutions, and multi-office firms (200+ users) with enterprise governance, compliance, and multi-brand management requirements.

**Monthly Pricing:** $38 per user/month  
**Annual Pricing:** $348 per user/year (23.7% discount)  
**Storage:** Unlimited  
**Minimum Users:** 50

#### Included Features
Everything in ClearDrive Professional, plus:
- **Multi-Brand Management**: Run unlimited branded portal domains from one admin console; ideal for multi-office accounting networks or holding companies with distinct subsidiaries.
- **Government ID Verification**: Clients prove identity via government-issued ID scan and liveness check before accessing high-risk portals (powered by Persona.com integration).
- **Regulatory Submission Rooms**: Structured submission environments for responding to SEC subpoenas, IRS audits, FINRA examinations, and GDPR data subject requests — with complete chain-of-custody documentation.
- Advanced DLP: detect and prevent upload or sharing of unencrypted financial data, SSNs, and credit card numbers.
- **Data Residency Controls**: Choose US-only, EU-only, or CA-only data storage per client workspace to meet jurisdictional requirements.
- HIPAA-compliant workspaces: BAA included, PHI handling procedures documented.
- Automated litigation hold: freeze all content across an entire client workspace on legal hold notice.
- **AI Document Summarization**: Automatically generate summaries of uploaded contracts, financial statements, and legal documents (powered by ClearDrive AI — document content never leaves your tenant).
- Custom SLA: 99.99% uptime guarantee with financial remedies.
- Dedicated ClearDrive implementation team (up to 40 hours onboarding included).
- Dedicated CSM and quarterly executive business reviews.
- 24/7 phone, chat, and email support with 1-hour critical SLA.
- Full REST API + Webhook support + Zapier integration (5,000+ no-code automations).
- Custom data processing agreements (DPA) for GDPR and CCPA.

#### Enterprise Add-Ons
| Add-On | Description | Pricing |
|---|---|---|
| ClearDrive Vault | Immutable long-term archive (WORM, 7–25 year retention) | $0.003/GB/month |
| White-Label Reseller | Full rebrand under partner's domain and branding | $500/month per brand |
| API Automation Pack | Higher API rate limits + dedicated API environment | $300/month |

---

## Technical Specifications

| Specification | Details |
|---|---|
| Storage Backend | Encrypted on AWS S3 (US, EU, CA regions) with optional customer-managed keys |
| Encryption at Rest | AES-256 |
| Encryption in Transit | TLS 1.3 |
| Maximum File Size | 5 GB (Starter), 50 GB (Professional), 250 GB (Enterprise) |
| Sync Client OS | Windows 10/11, macOS 11+, Ubuntu 18.04+ |
| Client Portal Access | Any modern browser, no client software required |
| Mobile OS | iOS 14+, Android 11+ |
| SSO Integration | SAML 2.0 (Okta, Azure AD, Google, OneLogin), OIDC |
| User Provisioning | SCIM 2.0 (Okta, Azure AD) |
| Audit Log Formats | JSON export; CSV export; webhook streaming |
| API | RESTful, OpenAPI 3.0 documented; Zapier, Make, Power Automate connectors |

---

## Compliance & Certifications

- SOC 2 Type II
- ISO/IEC 27001:2022
- PIPEDA compliant (Canada)
- GDPR (EU-US DPF; EU data center available)
- HIPAA BAA available
- CCPA compliant
- FINRA-aligned records retention capabilities

---

## Target Use Cases

1. **Accounting Firm Client Portal**: Clients upload tax documents via a branded, no-account portal; auto-checklists ensure complete packages; e-sign for engagement letters.
2. **Law Firm Secure File Exchange**: Share discovery documents with opposing counsel or clients with full audit trails and watermarking.
3. **M&A Virtual Data Room**: Create a governed data room with granular permissions, access tracking, and Q&A workflow for deal participants.
4. **Financial Advisor Document Collection**: Annually gather KYC/AML documents from clients with automated reminders and identity verification.
5. **Healthcare Patient Records Sharing**: HIPAA-compliant secure portal for sharing lab results, imaging, and referral documents with patients and specialist physicians.

---

## Pricing Summary

| Tier | Monthly (per user) | Annual (per user) | Storage |
|---|---|---|---|
| ClearDrive Starter | $10 | $96 | 1 TB/user |
| ClearDrive Professional | $22 | $208 | Unlimited |
| ClearDrive Enterprise | $38 | $348 | Unlimited |

*USD pricing. Canadian firms billed in CAD at prevailing exchange rate. Non-profit discount: 30% off list price.*

---

## Contact & Support

- **Sales:** sales@cleardrive.com | 1-855-CLEAR-99
- **Help Center:** help.cleardrive.com
- **Partner Program:** partners.cleardrive.com
- **Developer API:** api.cleardrive.com
