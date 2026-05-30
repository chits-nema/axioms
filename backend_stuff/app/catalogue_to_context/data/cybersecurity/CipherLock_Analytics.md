# CipherLock Analytics — Product Catalog

## Company Overview

CipherLock Analytics is a Chicago-based cybersecurity company founded in 2016, focused exclusively on data security, cloud security posture management (CSPM), and application security testing (AST). Unlike broad-platform vendors, CipherLock's thesis is depth over breadth: the company builds best-in-class tools for securing data at rest and in transit, scanning cloud environments for misconfigurations, and embedding security into software development pipelines (DevSecOps).

CipherLock serves 2,800 customers, predominantly in the technology, life sciences, and financial services sectors. The company has 620 employees and is backed by Sequoia Capital and General Catalyst. Annual revenue reached $195M in FY2025. CipherLock is a member of the Cloud Security Alliance (CSA) and co-authored the CSA's Cloud Controls Matrix v4.0.

Certifications: SOC 2 Type II, ISO 27001, CSA STAR Level 2, GDPR, HIPAA BAA available.

---

## Product Overview: CipherLock DataGuard Platform

The **CipherLock DataGuard Platform** is a cloud-native suite addressing three interconnected security disciplines: data discovery and classification, cloud security posture management, and application/API security testing. It is delivered entirely as SaaS with API-first design, making it a natural fit for engineering-led organizations building on AWS, Azure, and Google Cloud.

### Key Differentiators

- **DataSense AI**: Automated data discovery scans structured and unstructured data stores — databases, S3 buckets, SharePoint, Confluence — and applies 400+ built-in classifiers to tag sensitive data (PII, PHI, PCI, trade secrets).
- **CloudPosture Engine**: Continuously evaluates cloud infrastructure against 2,000+ security rules mapped to CIS Benchmarks, NIST 800-53, CSA CCM, SOC 2, and custom policies — with <5-minute detection of new misconfigurations.
- **ShiftLeft SAST/DAST/SCA**: Integrated Static Application Security Testing, Dynamic Application Security Testing, and Software Composition Analysis embedded directly into CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins, CircleCI).
- **API Security Testing**: Automatic API inventory discovery and active testing for OWASP API Top 10 vulnerabilities.
- **Risk Correlation Engine**: Connects a cloud misconfiguration (e.g., public S3 bucket) with the sensitivity of data stored in it — producing a prioritized, business-context-aware risk score rather than raw vulnerability counts.

---

## Solution Tiers

### Tier 1 — DataGuard Starter

**Ideal for:** Early-stage startups and small engineering teams (1–50 developers / up to 5 cloud accounts) that need foundational cloud security posture visibility and basic data scanning.

**Monthly Pricing:** $1,200/month (flat — up to 5 cloud accounts, 50 users)  
**Annual Pricing:** $12,000/year (16.7% discount)

#### Included Features
- CSPM for AWS, Azure, or GCP (1 cloud provider, up to 5 accounts)
- 800+ misconfiguration checks (CIS Benchmarks Level 1 and 2)
- Real-time alerting on critical/high severity misconfigurations
- Infrastructure-as-Code (IaC) scanning: Terraform, CloudFormation, Bicep (pull request integration)
- Data discovery scan: up to 10 data stores (S3, RDS, Azure Blob)
- PII and PCI data classification (100+ classifiers)
- Basic compliance dashboard: CIS AWS Foundations Benchmark
- 30-day finding history
- Slack and email notifications
- Email support (business hours, 48-hour SLA)

#### Limitations
- Single cloud provider only
- No application security testing (SAST/DAST/SCA)
- No API security
- No custom policy rules

---

### Tier 2 — DataGuard Professional

**Ideal for:** Scale-up technology companies and mid-market enterprises (50–500 developers, up to 25 cloud accounts) with multi-cloud environments and active software development.

**Monthly Pricing:** $4,800/month (up to 25 cloud accounts, 250 users)  
**Annual Pricing:** $48,000/year (16.7% discount)

#### Included Features
Everything in DataGuard Starter, plus:
- Multi-cloud CSPM: AWS + Azure + GCP simultaneously
- 2,000+ misconfiguration checks including container security (EKS, AKS, GKE) and serverless (Lambda, Azure Functions)
- Kubernetes security posture management (KSPM): CIS Kubernetes Benchmark
- **ShiftLeft SAST**: Static code analysis for 15 programming languages (Python, Java, Go, JavaScript/TypeScript, C#, Ruby, PHP, Kotlin, Swift, Rust, and more)
- **Software Composition Analysis (SCA)**: Open-source dependency scanning; CVSS-scored CVE alerts; SBOM generation (SPDX and CycloneDX)
- **DAST Lite**: Automated web application scanning for OWASP Top 10 (up to 5 applications)
- Data discovery: up to 100 data stores across cloud providers; 300+ classifiers including GDPR, HIPAA PHI, CCPA
- Risk correlation: link cloud misconfigurations to sensitive data exposure
- Compliance frameworks: CIS, NIST CSF, SOC 2 TSC, GDPR Article 32, HIPAA Security Rule
- 90-day finding history
- JIRA, GitHub Issues, ServiceNow ticket auto-creation for findings
- 24/7 chat support with 4-hour SLA

---

### Tier 3 — DataGuard Enterprise

**Ideal for:** Large enterprises, regulated financial institutions, and life sciences companies with 500+ developers, unlimited cloud accounts, and aggressive compliance and security posture requirements.

**Monthly Pricing:** Custom (starting at $18,000/month for baseline configuration)  
**Annual Pricing:** Custom; volume discounts based on cloud asset count and developer seats

#### Included Features
Everything in DataGuard Professional, plus:
- Unlimited cloud accounts and unlimited data store scanning
- **Full DAST**: Authenticated scan, API security testing (OWASP API Top 10, GraphQL, gRPC), continuous monitoring mode
- **API Inventory**: Auto-discover all internal and external APIs from traffic analysis and code scanning
- Secrets scanning: detect hardcoded credentials, API keys, and tokens in source code and CI artifacts
- Container image scanning: CVE scanning for Docker images in ECR, ACR, GCR, Docker Hub; runtime container drift detection
- **DataSense AI Advanced**: NLP-based unstructured data classification (documents, emails, Confluence pages, SharePoint)
- Data lineage mapping: track how sensitive data flows across systems and cloud services
- Custom policy engine: write custom CSPM and data policy rules in OPA (Open Policy Agent) Rego language
- Automated remediation: one-click or fully automated fixes for common misconfigurations (e.g., disable public S3 bucket ACL)
- Executive risk heatmap by cloud account, business unit, and application
- Compliance reporting automation: SOC 2, PCI DSS, HIPAA, ISO 27001, FedRAMP, NIST 800-53
- Dedicated Security Customer Success Manager and quarterly business reviews
- 24/7 phone/chat/email support with 1-hour critical SLA
- 365-day finding history + immutable audit trail
- Full REST API; Webhook support; Terraform, Pulumi, and CDK providers

#### Enterprise Add-Ons (Priced Separately)
| Add-On | Description | Pricing |
|---|---|---|
| DLP Agent | Endpoint and email DLP enforcement | +$8/user/month |
| Pen Test Orchestration | Managed penetration testing via partner network | Starting at $15,000/engagement |
| Red Team Exercises | CipherLock-facilitated adversary simulation | Custom |

---

## Technical Specifications

| Specification | Details |
|---|---|
| Cloud Integrations | AWS, Azure, GCP (agentless API-based) |
| IaC Support | Terraform, CloudFormation, Bicep, Pulumi, CDK |
| CI/CD Plugins | GitHub Actions, GitLab CI, Jenkins, CircleCI, Azure DevOps, Bitbucket Pipelines |
| Language Support (SAST) | Python, Java, JavaScript, TypeScript, Go, C#, Ruby, PHP, Kotlin, Swift, C/C++, Rust, Scala |
| Data Store Support | S3, Azure Blob, GCS, RDS (MySQL, Postgres, SQL Server), BigQuery, Snowflake, Redshift, DynamoDB, Cosmos DB, MongoDB Atlas |
| Classification Models | 400+ built-in; custom regex + ML model upload |
| Alert Latency | <5 minutes for new misconfiguration detection |
| Data Residency | US (primary), EU (Frankfurt), AP (Singapore) |
| SIEM Integration | Splunk HEC, Microsoft Sentinel, Sumo Logic, Datadog |

---

## Compliance & Certifications

- SOC 2 Type II
- ISO/IEC 27001:2022
- CSA STAR Level 2 Certified
- GDPR (Data Processor)
- HIPAA BAA available
- CCPA compliant

---

## Target Use Cases

1. **Cloud Misconfiguration Remediation**: Continuously scan for misconfigurations before attackers exploit them; reduce cloud security debt by 80% within 90 days.
2. **DevSecOps Pipeline Security**: Catch vulnerabilities at pull request stage; 94% of developers fix issues flagged by ShiftLeft without escalation to security team.
3. **Sensitive Data Sprawl Control**: Discover and inventory all sensitive data across 200+ cloud data stores before a breach reveals it.
4. **Compliance Automation**: Generate SOC 2 evidence collection packs automatically; reduce audit preparation time from weeks to hours.
5. **Open Source Risk Management**: Maintain an SBOM and receive real-time CVE alerts for third-party dependencies embedded in production software.

---

## Pricing Summary

| Tier | Monthly Price | Annual Price | Scope |
|---|---|---|---|
| DataGuard Starter | $1,200 | $12,000 | ≤5 cloud accounts, ≤50 users |
| DataGuard Professional | $4,800 | $48,000 | ≤25 cloud accounts, ≤250 users |
| DataGuard Enterprise | From $18,000 | Custom | Unlimited accounts and users |

*All prices in USD. Free 14-day trial available for Starter and Professional tiers (no credit card required).*

---

## Contact & Support

- **Sales:** sales@cipherlock.io | 1-312-CIPHER-1
- **Developer Portal:** dev.cipherlock.io
- **Community Slack:** community.cipherlock.io
- **CVE Disclosure:** security@cipherlock.io
