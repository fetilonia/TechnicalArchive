---
hide:
  - navigation
---

# Microsoft Technical Archive

<div class="hero-copy" markdown>

Microsoft 플랫폼에 대한 **Architecture, Implementation, Investigation, Validation, Operations** 지식을 축적하는 Technical Knowledge Base입니다.

이 사이트의 콘텐츠는 Notion의 **Microsoft Technical Archive**와 그 하위 페이지만을 source of truth로 사용합니다.

</div>

<div class="grid cards" markdown>

-   :material-microsoft-azure:{ .lg .middle } **Azure**

    ---

    Entra ID, Global Secure Access, Microsoft Sentinel, Identity 및 Cloud Security.

    [Explore Azure →](azure/index.md)

-   :material-account-key:{ .lg .middle } **Identity & Access**

    ---

    Authentication, Conditional Access, WHfB, Hybrid Identity, Administrative Unit.

    [Explore Entra ID →](azure/entra-id/index.md)

-   :material-powershell:{ .lg .middle } **PowerShell**

    ---

    운영 자동화, 검증 스크립트, Microsoft Graph 기반 engineering tools.

    [Explore PowerShell →](powershell/index.md)

-   :material-shield-search:{ .lg .middle } **Security Operations**

    ---

    Microsoft Sentinel, hunting, search rules, evidence-driven investigation.

    [Explore Sentinel →](azure/sentinel/index.md)

</div>

## Featured technical articles

- [민감한 Resource 접근 시 인증강도 정책에 Windows Hello for Business 인증 조합 사용](azure/entra-id/whfb-authentication-strength.md)
- [Global Secure Access 기반 Universal Tenant Restrictions 구현 및 검증](azure/global-secure-access/universal-tenant-restrictions.md)
- [Administrative Unit Feature Matrix](azure/entra-id/administrative-unit-feature-matrix.md)
- [Sentinel Data Lake 구성](azure/sentinel/data-lake.md)

## Library model

```text
Microsoft Technical Archive
├─ Product / Platform
│  ├─ Technology domain
│  │  ├─ Architecture
│  │  ├─ Technical guide
│  │  ├─ Investigation
│  │  ├─ Validation
│  │  └─ Tool / Code
```

!!! info "Source boundary"
    `Project Archive`와 고객사 프로젝트 영역은 이 사이트의 검색, fetch, migration 대상에서 제외됩니다.
