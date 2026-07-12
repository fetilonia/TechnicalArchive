---
title: 민감한 Resource 접근 시 인증강도 정책에 Windows Hello for Business 인증 조합 사용
type: TechnicalGuide
domain: Identity
product:
  - Microsoft Entra ID
  - Windows Hello for Business
status: Migrated - assets pending
source_page_id: 37fdbd59-1ead-8021-b6d0-c048ceec181b
last_source_edit: 2026-06-14
---

# 민감한 Resource 접근 시 인증강도 정책에 Windows Hello for Business 인증 조합 사용

Hybrid AD Join Windows 환경에서 Windows Hello for Business PIN 기반 인증을 구현하고, Conditional Access Authentication Strength 조건을 만족하는지 검증하는 기술 문서입니다.

| Metadata | Value |
|---|---|
| Document type | Technical Guide / Validation |
| Source status | 완료 |
| Source hierarchy | Microsoft Technical Archive → Azure → EntraID |
| Last source edit | 2026-06-14 |
| Asset state | Notion export binary import required |

## Objective

On-premises AD와 Microsoft Entra ID 간 Microsoft Entra Kerberos 또는 Cloud Kerberos Trust를 구성한 뒤 다음 상태를 검증합니다.

- Hybrid Join
- Primary Refresh Token
- WHfB provisioning
- CloudTgt
- OnPremTgt
- Conditional Access Authentication Strength satisfaction

## Scope distinction

!!! warning "Passkey and WHfB are separate deployment controls"
    Passkey (FIDO2)는 WHfB와 동일한 정책으로 배포되는 기능이 아닙니다. Microsoft Entra ID의 Authentication methods policy에서 별도로 활성화하며, 본 문서의 주 범위는 WHfB PIN 기반 인증입니다.

## Environment assumptions

- Client management: AD Group Policy
- Device state: Hybrid Microsoft Entra joined
- Authentication: Microsoft Entra ID and on-premises AD
- Validation target: privileged Microsoft Graph access protected by Authentication Strength

## FIDO2 authentication method

### Enable the FIDO2 policy

Microsoft Entra admin center에서 다음 경로를 사용합니다.

```text
Entra ID
└─ Authentication methods
   └─ Policies
      └─ Passkey (FIDO2)
```

정책 배포 대상은 group 단위로 지정할 수 있으며, 운영 전 다음 설정을 확정해야 합니다.

- Self-service setup
- Allowed passkey types
- Attestation requirement
- Key restriction policy
- Pilot group scope

!!! caution "Asset preservation"
    원본 단계별 screenshot은 Notion signed URL을 직접 참조하지 않습니다. Notion export에서 binary를 가져와 `docs/assets/notion/<page-id>/`에 복제하고 SHA-256 검증 후 표시합니다.

## WHfB provisioning

### Policy deployment

WHfB 정책은 AD Group Policy 기반으로 배포하며, credential registration과 device state를 함께 확인합니다.

### Client verification

```powershell
dsregcmd /status
```

검증 대상:

```text
AzureAdJoined
DomainJoined
AzureAdPrt
NgcSet
CloudTgt
OnPremTgt
```

## Conditional Access validation

### Allowed path

- WHfB key credential 등록 완료
- PRT 발급 완료
- Authentication Strength에 WHfB 허용
- 대상 resource 접근 성공

### Blocked path

- password-only session
- WHfB provisioning 미완료
- 인증강도 요구 불충족
- target resource 접근 차단 또는 step-up 요구

## Evidence classification

!!! success "Confirmed observation"
    Source 문서에서 Hybrid Join, PRT, WHfB provisioning, CloudTgt 및 OnPremTgt 상태를 검증 대상으로 정의했습니다.

!!! info "Documented behavior"
    FIDO2와 WHfB는 별도의 authentication method 및 deployment control로 취급합니다.

!!! warning "Technical inference"
    Authentication Strength 성공 여부는 credential 등록만이 아니라 token/session 상태와 target resource policy evaluation을 함께 검증해야 합니다.

## Verification checklist

- [ ] Device Hybrid Join 확인
- [ ] PRT 발급 확인
- [ ] WHfB credential 등록 확인
- [ ] CloudTgt / OnPremTgt 확인
- [ ] Authentication Strength policy assignment 확인
- [ ] password-only blocked path 확인
- [ ] WHfB allowed path 확인
- [ ] Sign-in log authentication details 확인
- [ ] Source screenshot binary hash 검증

## Source

[Open source page in Notion](https://app.notion.com/p/37fdbd591ead8021b6d0c048ceec181b)
