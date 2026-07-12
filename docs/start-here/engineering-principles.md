# Engineering Principles

## Evidence before conclusion

관찰된 현상과 결론을 분리하고, 동일 사용자·시간·클라이언트·workload 기준으로 증적을 교차 검증합니다.

## Validate assumptions

Portal 상태, PowerShell/API 결과, 로그, HAR/ETL 결과를 독립적으로 확인합니다.

## Control plane is not enforcement

정책을 구성한 관리 plane과 실제 접근을 통제하는 workload enforcement를 분리합니다.

## Read-only before change

가장 작은 read-only test부터 수행하며 변경은 최소 범위와 가역성을 우선합니다.

## Root cause over workaround

조치 후 정상화만으로 root cause를 확정하지 않습니다.

## Automation follows engineering

자동화는 문제 정의, 안전 경계, rollback, verification이 확정된 이후 적용합니다.
