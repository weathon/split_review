## Summary

This paper re-implements Critic-Guided Decision Transformers (CGDT) and Online Decision Transformers (ODT) for the Gym‑μRTS environment, proposes a combined method called Online Critic-Guided Decision Transformer (OCGDT), and creates a dataset of 3,000 trajectories from games between two rule‑based bots. The agents are evaluated against benchmark bots and compared with Implicit Q‑Learning (IQL). The authors claim OCGDT matches IQL’s performance with fewer wall‑clock training hours.

## Strengths

- **Thorough experimental setup:** The paper includes detailed ablation studies that isolate the contributions of online fine‑tuning, context length, and offline training duration, providing a clear picture of how each component behaves in this setting.
- **Honest discussion of limitations:** Sections 5.1 and 6 openly discuss the ineffectiveness of online fine‑tuning on this dataset, overfitting issues, and the lack of improvement from the proposed combination. This transparency is valuable.
- **Reproducibility effort:** The authors provide code, hyper‑parameter configurations, and a dataset, which is commendable and supports future work in the μRTS domain.

## Weaknesses

### Major

1. **No significant improvement over existing methods.**  
   OCGDT does not outperform its components (CGDT, ODT) on the main benchmark bots; all confidence intervals overlap substantially (Table 1). Cross‑agent win rates also show OCGDT essentially tied with CGDT and ODT (Table 2). The claimed advantage over IQL is marginal and inconsistent (e.g., OCGDT achieves 26.2% vs. CoacAI while IQL 800k gets 21.5%, but against Mayari IQL 800k obtains 42.6% vs. OCGDT’s 40.1%). The central novelty—combining critic guidance with online fine‑tuning—does not yield clear empirical benefit.

2. **Unsupported main claim of efficiency.**  
   The paper states OCGDT “matches the performance of IQL in half the wall‑clock hours,” but the comparison is not apples‑to‑apples. IQL 800k (9 hours) uses purely offline training, while OCGDT (4.25 hours) includes online environment interactions whose cost is not accounted for in terms of environment steps or sample collection time. The more directly controlled comparisons (IQL 400k, same wall‑clock; IQL 13k, same gradient updates) show OCGDT ahead, but the paper does not disentangle whether the advantage comes from the critic guidance, the online fine‑tuning, or simply the different architectural inductive biases of transformers vs. MLPs.

3. **Limited novelty for ICLR.**  
   The paper applies two existing DT extensions (CGDT, ODT) to a specific environment and combines them with a straightforward additive loss (Equation 11) that is essentially a weighted sum of the two previous objectives. There is no new algorithmic insight, theoretical analysis, or empirical finding that generalises beyond μRTS. The core result (OCGDT ≈ IQL ≈ CGDT ≈ ODT on these tasks) is more of a negative or null finding than a forward contribution.

4. **Online fine‑tuning is not beneficial under the studied conditions.**  
   Ablation OCGDT D (no fine‑tuning) performs comparably to the full OCGDT, and extended fine‑tuning (OCGDT B, C) degrades or does not improve. This undermines a major motivation for the proposed method and suggests the online component is unnecessary with this dataset. The paper does not investigate *why* fine‑tuning fails (e.g., poor exploration, sparse rewards, small buffer) beyond hypothesising about buffer pollution.

### Minor

- The critic loss asymmetry formulation (Equation 4) is written with $u$ appearing inside the indicator, but the indicator condition $(u > 0)$ seems inconsistent with the text (“penalises over‑estimates if $u < 0$”). The notation may benefit from clarification, though this is likely a copy‑editing issue.
- The evaluation uses only 400 games per match‑up (4 seeds × 100 games). Confidence intervals are ±4–5%, making it hard to reliably rank methods that differ by only a few percentage points.
- The dataset is generated from only two scripted bots (CoacAI and Mayari) and the policy is evaluated on those same bots plus IQL. Generalisation to other bot styles or human players is not demonstrated.

### Trivial

- The parameter $\tau_p$ in Equation 5 is called the “expectile asymmetry parameter” but it plays the role of a weighting factor in a squared loss, which is not exactly the usual definition of an expectile; this is a minor terminology inconsistency.

## Nice-to-Haves

- Provide the total number of environment interactions (online steps) for OCGDT to enable a fairer sample‑efficiency comparison.
- Include a baseline using a simple behavioural cloning (BC) policy trained on the same dataset to understand whether the transformer architecture itself drives performance.
- Investigate why the online phase degrades performance—e.g., by tracking the average return‑to‑go of trajectories in the replay buffer over time.

## Novel Insights

None beyond the paper’s own contributions. The main empirical finding is that on this µRTS dataset, CGDT, ODT, OCGDT, and IQL achieve statistically similar win rates, with the online component of OCGDT providing no measurable benefit. This is a useful negative result for the µRTS community but does not constitute a novel insight for the broader RL or sequence‑modeling field.

## Suggestions

- Focus the narrative on the empirical comparison of DT‑based methods in µRTS rather than claiming an algorithmic advance. The paper would be stronger as a reproducibility/benchmarking report.
- Run the fine‑tuning phase with a much larger replay buffer or using offline data only to determine whether the online component can ever improve performance.

## Score and Decision

**Score:** 4.0

**Decision:** Reject

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>