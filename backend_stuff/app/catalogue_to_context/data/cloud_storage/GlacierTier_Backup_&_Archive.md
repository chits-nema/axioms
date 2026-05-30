# GlacierTier Backup & Archive — Product Catalog

## Company Overview

GlacierTier Backup & Archive is a Minneapolis-based cloud backup, disaster recovery, and long-term archival company founded in 2009. Unlike collaboration-focused cloud storage vendors, GlacierTier's products are built exclusively for data protection: reliable backup of servers, endpoints, databases, virtual machines, Microsoft 365, and Google Workspace with fast, predictable recovery.

GlacierTier serves 21,000 customers globally, predominantly through managed service providers (MSPs) and IT resellers, though it also sells direct to enterprise IT teams. The company employs 680 people and processes 4.8 petabytes of backup data per day. In 2025, GlacierTier customers performed 1.2 million recovery operations with an average recovery time of 4.3 minutes. The company is profitable and bootstrapped (no outside investment), with $230M in ARR for FY2025.

Certifications: SOC 2 Type II, ISO 27001, HIPAA BAA available, PCI DSS applicable controls, Cyber Essentials Plus (UK).

---

## Product Overview: GlacierTier DataProtect Suite

The **GlacierTier DataProtect Suite** is a unified backup-as-a-service platform that protects physical servers, virtual machines (VMware vSphere, Microsoft Hyper-V, Nutanix AHV), Windows/macOS endpoints, cloud workloads (AWS EC2, Azure VMs), databases (SQL Server, MySQL, PostgreSQL, Oracle), and SaaS data (Microsoft 365, Google Workspace, Salesforce) — all from a single multi-tenant management console.

### Key Differentiators

- **Instant Recovery**: Spin up a protected VM or server directly from the GlacierTier cloud backup within 90 seconds — no data restore required until planned failback.
- **Ransomware-Proof Architecture**: Immutable backups using Object Lock (WORM); anomaly detection flags sudden encryption of backup data; isolated recovery copies in air-gapped vault.
- **30-Second Backup Increments**: Continuous Data Protection (CDP) for mission-critical VMs and databases — recovery point objective (RPO) as low as 30 seconds.
- **MSP Multi-Tenant Console**: GlacierTier is built for MSPs — centralized billing, per-client reporting, white-label client portals, and role-based access delegation.
- **WAN-Optimized Deduplication**: Global deduplication and compression reduce backup storage consumption by an average of 65% and bandwidth requirements by 80%.

---

## Solution Tiers

### Tier 1 — DataProtect Essentials

**Ideal for:** Small businesses, home offices, and SMBs with straightforward server and endpoint backup needs and limited IT resources.

**Monthly Pricing:**
- Server backup: $25/server/month (up to 1 TB included storage per server)
- Endpoint backup: $5/device/month (up to 200 GB included per device)
- Additional storage: $0.06/GB/month (Standard); $0.015/GB/month (Archive class, 90-day minimum retention)

**Minimum Commitment:** None (pay-as-you-go)

#### Included Features
- Agent-based backup for Windows Server (2012 R2+), Windows 10/11, macOS (11+)
- Daily incremental backups (scheduled; minimum interval: 1 hour)
- Block-level deduplication and compression (client-side)
- File and folder restore (self-service, web portal)
- Bare-metal restore (BMR) to new hardware
- 30-day retention included; configurable up to 1 year
- Encryption: AES-256 in transit (TLS 1.3) and at rest; customer passphrase option (keys held client-side)
- GlacierTier cloud storage hosted in US-East (Virginia) default
- 1 cloud storage region per account
- Self-service management portal
- Email alert on backup failure
- Email support (business hours, 48-hour SLA)
- Recovery testing report: monthly automated restore verification

#### Limitations
- No VM backup (VMware/Hyper-V)
- No database-aware backup (VSS only for SQL Server)
- No SaaS backup (Microsoft 365, Google Workspace)
- No instant cloud recovery/spin-up

---

### Tier 2 — DataProtect Advanced

**Ideal for:** SMBs and mid-market companies (5–500 servers) with virtualized infrastructure, SQL/Exchange databases, and recovery time requirements measured in minutes.

**Monthly Pricing:**
- Server/VM backup: $45/server or VM/month (up to 2 TB included storage)
- Endpoint backup: $8/device/month (up to 500 GB included)
- Microsoft 365 backup: $3.50/user/month (Exchange, OneDrive, SharePoint, Teams)
- Google Workspace backup: $3.50/user/month (Gmail, Drive, Calendar, Contacts)
- Additional storage: $0.05/GB/month (Standard); $0.012/GB/month (Archive)

#### Included Features
Everything in DataProtect Essentials, plus:
- **VMware vSphere backup**: agentless backup of VMs via vSphere API; Changed Block Tracking (CBT) for incremental efficiency
- **Microsoft Hyper-V backup**: agentless; supports Hyper-V 2016, 2019, 2022
- Nutanix AHV VM backup
- Application-aware backup: Microsoft SQL Server (transaction-log backup, point-in-time recovery to any transaction), Exchange Server, Active Directory, SharePoint
- **Instant VM Recovery**: Boot a VM backup image in GlacierTier cloud in <90 seconds; run indefinitely or failback when ready
- Granular Exchange and Active Directory recovery: restore individual mailboxes, mailbox items, AD objects, and GPOs
- **Microsoft 365 Backup**: Unlimited retention for Exchange Online, OneDrive, SharePoint Online, Teams messages and channels
- **Google Workspace Backup**: Gmail (unlimited retention), Google Drive, Calendar, Contacts
- Cross-region replication: replicate backups to a second cloud region for DR
- Retention policies: grandfather-father-son (GFS) scheduling, compliance hold
- Immutable backup copies (Object Lock WORM mode, configurable retention)
- 90-day retention included; configurable up to 7 years
- 24/7 chat and email support with 4-hour SLA
- 99.9% storage durability SLA

---

### Tier 3 — DataProtect Enterprise

**Ideal for:** Large enterprises, healthcare organizations, financial institutions, and MSPs managing backup for 50+ customers or 1,000+ protected workloads.

**Monthly Pricing:** Custom committed pricing  
**Starting Price:** $8,000/month (baseline for 100 servers/VMs + 1,000 endpoints + 500 Microsoft 365 users)  
**Volume Discounts:** Significant at 500+ servers and 5,000+ endpoints

#### Included Features
Everything in DataProtect Advanced, plus:
- **Continuous Data Protection (CDP)**: 30-second RPO for mission-critical VMs and SQL Server — journal-based continuous backup with any-point-in-time recovery
- **Air-Gapped Vault**: Isolated, write-once backup copy stored in a physically separated GlacierTier vault segment; immune to ransomware, admin error, and malicious insider
- Salesforce backup: full org backup (objects, attachments, metadata); record-level restore; sandbox seeding
- AWS EC2 and Azure VM backup (agentless, cross-account)
- Oracle Database backup: RMAN-integrated; table-level restore
- PostgreSQL and MySQL backup: binary log capture for continuous protection; schema and row-level restore
- **Instant Failover to Cloud (DRaaS)**: Failover production environment to GlacierTier cloud within 15 minutes; run production from cloud during outage; failback on recovery
- Network configuration backup: Cisco, Juniper, Palo Alto, Fortinet device configs on schedule
- Multi-tenant MSP console: per-client billing, isolation, reporting, and branding; bulk policy management
- **GlacierTier Canary Testing**: Weekly automated test recovery of randomly selected backup sets; results emailed with screenshots — prove backups work before you need them
- Ransomware detection: ML-based anomaly detection flags unusual data change patterns that indicate active encryption
- Compliance reports: HIPAA, PCI DSS, SOX, ISO 22301 (business continuity)
- Dedicated Customer Success Engineer and monthly operational reviews
- 24/7 phone, chat, and email support with 1-hour critical SLA
- 99.999% storage durability (multi-region redundancy)

#### MSP Partner Pricing
GlacierTier offers wholesale pricing for MSP partners managing multiple client accounts:
- Registered Partner (0–50 clients): 15% discount off list
- Silver Partner (51–150 clients): 25% discount + co-branded portal
- Gold Partner (151+ clients): 35% discount + dedicated partner manager + co-marketed case studies

---

## Technical Specifications

| Specification | Details |
|---|---|
| Supported Virtualization | VMware vSphere 6.7+, Hyper-V 2016+, Nutanix AHV 5.20+ |
| Supported OS (Agent) | Windows Server 2012 R2–2025, Windows 10/11, macOS 11–14, RHEL/CentOS/Ubuntu LTS |
| Backup Protocols | VSS (Windows), BTRFS snapshots (Linux), vSphere API, Hyper-V WMI |
| Database Support | SQL Server 2014–2022, Exchange 2013–2019, Oracle 12c–19c, PostgreSQL 11–16, MySQL 5.7/8.0, MongoDB 4.4+ |
| SaaS Backup | Microsoft 365 (Exchange, OneDrive, SharePoint, Teams), Google Workspace, Salesforce |
| Deduplication Ratio | 3:1 to 10:1 typical (global dedup across protected sources) |
| Compression Ratio | 1.5:1 to 3:1 typical |
| Instant Recovery Boot Time | <90 seconds (VM spin-up) |
| CDP Minimum RPO | 30 seconds |
| DRaaS RTO | <15 minutes (Enterprise) |
| Data Centers | US-East (VA), US-West (OR), EU-Central (Frankfurt), UK-South (London), AP-Southeast (Sydney) |
| Encryption | AES-256 at rest; TLS 1.3 in transit; optional passphrase key (client-held, zero-knowledge) |

---

## Compliance & Certifications

- SOC 2 Type II
- ISO/IEC 27001:2022
- HIPAA BAA available
- Cyber Essentials Plus (UK)
- GDPR compliant (EU data centers available)
- ISO 22301 aligned (Business Continuity Management)

---

## Target Use Cases

1. **Ransomware Recovery**: Immutable WORM backups and air-gapped vault provide recovery copies that ransomware cannot reach; average recovery time <2 hours.
2. **Microsoft 365 Data Protection**: Microsoft does not guarantee M365 data recovery beyond 30 days — GlacierTier provides unlimited-retention backup.
3. **Disaster Recovery as a Service**: Instant VM failover to GlacierTier cloud meets aggressive RTO/RPO requirements without a secondary data center.
4. **MSP Managed Backup**: White-label multi-tenant console allows MSPs to manage 100+ client backup environments with per-client billing and reporting.
5. **Database Point-in-Time Recovery**: SQL Server transaction log backup enables recovery to within 1 minute of a data corruption event.

---

## Pricing Summary

| Tier | Servers | Endpoints | M365 Users | Starting Monthly |
|---|---|---|---|---|
| Essentials | $25/server | $5/device | Not included | Pay-as-you-go |
| Advanced | $45/server/VM | $8/device | $3.50/user | Pay-as-you-go |
| Enterprise | Custom | Custom | Custom | ~$8,000/month |

*USD pricing. Free 30-day trial (up to 5 servers + 25 endpoints). MSP wholesale pricing available.*

---

## Contact & Support

- **Sales:** sales@glaciertier.com | 1-800-GLACIER
- **MSP Partner Program:** msps.glaciertier.com
- **Status Page:** status.glaciertier.com
- **Restore Help:** recover.glaciertier.com
