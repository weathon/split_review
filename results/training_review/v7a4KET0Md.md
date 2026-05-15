Now I have all the information I need. Let me compile the final consolidated review.

## Summary
The paper introduces SWIRL (SWitching IRL), an inverse reinforcement learning framework that models animal behavior as sequences of short-term decision-making processes, each governed by a distinct reward function. SWIRL incorporates two forms of history dependency: (1) **decision-level**: state-dependent transitions between hidden modes (which decision process the animal is in), and (2) **action-level**: non-Markovian rewards/policies within each mode that depend on the previous state (L=2). The model is evaluated on a simulated gridworld, a 127-node labyrinth with water-restricted mice, and a spontaneous behavior dataset.

---

## Strengths

- **Biologically motivated framework with two levels of history dependency**: SWIRL explicitly models both decision-level (mode transitions depend on current state, preventing rapid switching) and action-level (reward depends on current and previous state) history. This dual-level design is concretely motivated by real animal behavior constraints, such as the once-per-90s water reward in the labyrinth (lines 14, 66). The variants I-1/I-2/S-1/S-2 allow systematic ablation of each component.

- **Interpretable, semantically meaningful inference on real animal data**: On the labyrinth dataset, SWIRL (S-2) recovers reward maps (water, home, explore) whose spatial patterns align with known experimental design, including a history-dependent water reward that correctly captures the "once-per-visit" constraint — high reward when arriving at the water port, higher reward for leaving it (Fig. 3C). Hidden-mode segments consistently align with water-port visits and home visits without prior knowledge of those locations (lines 80-85). This demonstrates the framework's practical utility for hypothesis generation in neuroscience.

- **Honest handling of a negative result**: On the spontaneous behavior dataset, models with action-level history (S-2, I-2) produce lower test log-likelihood than their Markovian counterparts (S-1, I-1). Rather than suppressing this, the paper explicitly discusses it and attributes it to preprocessing choices (merging consecutive identical syllables), and reframes SWIRL as a hypothesis-testing tool (lines 93-95). This scientific candor strengthens the paper's credibility.

- **Demonstrated on longer, more complex trajectories than prior IRL applications to this domain**: The labyrinth data is processed into 500-step trajectories across a 127-node graph, a scale that the paper correctly notes is "considerably greater challenge" compared to prior work limited to "clustered, stereotyped trajectories of only 20 time points" (line 76).

---

## Weaknesses

### Fatal
None.

### Major

- **Inference procedure is under-specified — M-step for reward learning is not described**: Section 3.4 presents the EM auxiliary function (E-step) and mentions the forward-backward algorithm for mode inference, but never specifies how the reward functions \(r_z\) are updated in the M-step. The paper states "If we have estimated the current policy \(\pi_{z_n}\) based on the current reward estimate \(r_z\)" (line 37) without explaining how \(r_z \to \pi_z\) is computed for general MDPs. Soft-Q iteration is mentioned only for the gridworld simulation (line 66). For the real datasets, the reader is left to infer the algorithm. This is a reproducibility gap — the core inference loop is incomplete without specifying how the inner IRL problem (solving for policy from reward) is solved, how the reward parameters are structured/parameterized, and how the EM alternates between these steps.

- **Evaluation relies heavily on ablations with limited external IRL baselines**: The only non-SWIRL IRL baseline is MaxEnt (single-mode IRL). Multi-intention IQL and Locally Consistent IRL are subsumed as SWIRL variants (I-1, S-1). The other comparators (ARHMM, rARHMM) are dynamics-based models, not IRL methods. This means the evaluation primarily demonstrates that the full SWIRL (S-2) outperforms its own ablations. Without a competitive, non-ablation time-varying IRL baseline (e.g., BNP-IRL, Dynamic IRL), it is difficult to assess whether the improvements come from the specific contributions (history dependency, state-dependent transitions) or simply from the overall SWIRL architecture. This is particularly relevant because the advantage of action-level history (L=2 over L=1) is inconsistent across datasets.

### Minor

- **Abstract's claim is too sweeping relative to full results**: The abstract states SWIRL "outperforms models lacking history dependency, both quantitatively and qualitatively" as a general finding. However, on the spontaneous behavior dataset, action-level history dependency (S-2, I-2) _underperforms_ its Markovian counterparts (S-1, I-1). While the paper discusses this honestly in Sections 4.3 and 5, the abstract's unqualified claim misrepresents the evidence. A more precise statement would note that history dependency helps on some datasets (simulated gridworld, labyrinth) but not others, and the framework enables testing this question.

- **No statistical significance measures for labyrinth results**: The labyrinth held-out test log-likelihood comparison (Fig. 3E) is reported via box plots with overlapping distributions, but no formal significance tests or confidence intervals are provided. The improvement of S-2 over the next-best model appears visually modest, and without significance testing the reader cannot assess whether this improvement is reliable.

- **Discussion is too brief with no limitations**: Section 5 is only a few sentences and contains no discussion of limitations, failure modes, computational cost, sensitivity to hyperparameters (e.g., the choice of K, the history length L=2), or comparison to alternative frameworks (e.g., Bayesian approaches). Including a limitations paragraph would significantly strengthen the paper.

### Trivial

- **Choice of hidden mode count K is not justified**: The paper uses K=3 for the labyrinth and K=5 for spontaneous behavior without explaining how these values were selected or whether results are sensitive to this choice.

- **No sensitivity analysis on preprocessing choices**: The labyrinth preprocessing (238 trajectories of 500 time points) and spontaneous behavior preprocessing (merging consecutive identical syllables, selecting top 9) are described but their impact on results is not explored. For instance, the paper's own explanation for the negative spontaneous behavior result relies on the preprocessing — this could be tested directly.

---

## Nice-to-Haves

- A complete pseudocode or derivation of the EM algorithm, especially the M-step for reward learning, to ensure reproducibility.
- A competitive non-ablation time-varying IRL baseline (e.g., BNP-IRL, DIRL) to better contextualize SWIRL's improvements.
- Significance tests (e.g., bootstrap confidence intervals) for the labyrinth LL comparison.
- Sensitivity analysis on K (number of hidden modes) and on preprocessing choices (different history lengths L>2, different trajectory segmentation strategies).
- A dedicated limitations paragraph in the Discussion.

---

## Removed Points
*These points are flagged to be removed — treat them with caution.*

1. **"Novelty claim about being first IRL model with history-dependent rewards is false"** — REMOVED. The critic cites specific papers (Michini & How 2012, Choi & Kim 2012) not referenced in the paper. Per guidelines, I cannot verify whether these constitute genuine prior IRL work on non-Markovian rewards. The paper's claim is specifically about *IRL* (not RL), and the paper acknowledges history dependency in RL via Houthooft et al. (2016) and Sharafeldin et al. (2024). Without external verification of the cited prior IRL work, this criticism cannot be substantiated.

2. **"Missing Section 3.5"** — REMOVED. The paper references Sec. 3.5 in lines 15 and 91, and its absence in the extracted text is a parser artifact, not an author omission. Per guidelines, parser artifacts should not be treated as author errors.

3. **"Preprocessing of labyrinth dataset is not described"** — REMOVED. The paper does describe it: "we segmented the raw node visit data into 238 trajectories, each comprising 500 time points" (line 76). The description could be more detailed but is not absent.

4. **"Spontaneous behavior preprocessing removes temporal dependencies"** — REMOVED. The paper already acknowledges and discusses this exact concern, explicitly stating: "We believe this is attributable to the merging of consecutive identical syllables and the selection of the top 9 syllables during the preprocessing phase" (line 93). The authors cannot be faulted for a limitation they already identify and discuss.

5. **"Missing non-Markovian IRL in related work section"** — REMOVED. Per guidelines, I cannot verify the existence or relevance of unspecified prior work.

6. **"Formatting/style nitpicks" and "typos/spelling/grammar"** — REMOVED. Per guidelines, these are likely parser artifacts.

---

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the method or results that the paper itself does not already articulate.

---

## Suggestions

1. **Specify the M-step**: Provide a clear description or pseudocode for how reward parameters are updated in the EM algorithm. State which IRL algorithm (e.g., MaxEnt IRL with soft value iteration, or another method) is used to derive policies from rewards in each mode for the general case, not just the gridworld.

2. **Add at least one competitive time-varying IRL baseline** (e.g., BNP-IRL or DIRL) to the main experiments to contextualize SWIRL's performance beyond its own ablations.

3. **Qualify the abstract's claim**: Replace the sweeping statement about outperformance with a more measured claim, e.g., "SWIRL outperforms models lacking history dependency on simulated and labyrinth datasets, and provides a framework for testing whether history dependency is present in a given dataset."

4. **Add statistical significance tests** (or confidence intervals) for the labyrinth test log-likelihood comparison.

5. **Include a brief limitations section** in the Discussion, addressing sensitivity to K, the L=2 restriction, and the role of preprocessing choices.

---

## Score and Decision

This paper addresses a genuine gap — modeling time-varying, history-dependent reward functions in animal behavior — and demonstrates the framework on non-trivial real-world data with interpretable results. However, two structural issues prevent a stronger assessment: (1) the inference procedure is incompletely specified (the M-step for reward learning is absent), creating a reproducibility gap, and (2) the evaluation relies primarily on ablations of the authors' own model variants with limited external baselines, making it difficult to assess the marginal contribution relative to prior time-varying IRL approaches. The strengths (biologically motivated design, interpretable results on real data, honest treatment of a negative result) are real, but the paper would benefit from substantial revisions to address the specification and evaluation gaps before it can be considered fully solid.

**Score: 5.5 / 10** — A methodologically interesting contribution with promising applications, but the underspecified inference procedure and limited comparative evaluation weaken the evidence. The paper provides a useful framework and interesting qualitative insights, but falls short of the fully rigorous empirical validation needed to support its strongest claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>