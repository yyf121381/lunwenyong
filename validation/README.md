# Validation results

Three evidence classes are reported separately. Do not combine them into a single “pass rate”.

| Class | Files | Scale | Model involved? |
|---|---|---|---|
| Deterministic | `deterministic/README.md`, `../repro/` | 6 chain cases + 10 unit checks | No |
| Assembly | `assembly/README.md` | 6/6 real-assembly cases | No live model; declared model output |
| Canary | `canary/README.md` | 3 real-entry turns, one account | Yes (`deepseek-flash`) |

The deterministic class proves code-path behavior under fixed inputs. The assembly class proves the real chain (decision core → audit → repair → validation) passes for fixed cases. The canary class proves three real entry turns were delivered normally; it does not prove window isolation, production rates, or scale.
