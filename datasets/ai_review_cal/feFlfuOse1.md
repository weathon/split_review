- Decision: Reject
- Avg Score: 7.25
- Scores: 5, 10, 6, 8
Good — confirmed: no error bars, variance, or multiple-run methodology is mentioned anywhere in the paper; no limitations section exists. Now I have all the information needed to write the final consolidated review.

---

## Summary

This paper describes Gymnasium, an open-source library that provides a standardized API for reinforcement learning environments, forked from OpenAI Gym. It highlights several design contributions: a functional API (FuncEnv) that maps cleanly onto POMDP components, a clear separation of episode termination and truncation signals, algebraic composite spaces (sum/product types), and a first-class vectorization abstraction. The paper also catalogs the built-in benchmark environments.

## Strengths

- **Explicit termination/truncation separation with clear practical motivation (Section 4.2):** The paper identifies a subtle but important ambiguity in the predecessor API and provides a concrete racing example showing how conflating state-based termination with time-based truncation leads to incorrect value estimation in algorithms like PPO and DQN. The pedagogical value of this explanation is high and directly serves practitioners.

- **Functional API with clean POMDP mapping (Section 4.1):** The `FuncEnv` abstraction decomposes environment interaction into `initial`, `observation`, `transition`, `reward`, and `terminal` functions that correspond one-to-one with POMDP components, contrasting with the object-oriented `Env` where `reset` and `step` conflate multiple components. This is a concrete design improvement for theoretical clarity and potential hardware acceleration.

- **Algebraic spaces formalization (Section 4.3):** The introduction of `Tuple` (product type) and `OneOf` (sum type) as composite spaces that mirror algebraic data types is a genuinely new feature absent from OpenAI Gym, enabling cleaner representation of environments with disjoint observation/action modalities.

- **Vectorization as a first-class abstraction with benchmarks (Section 4.4, Figures 1–2):** The paper demonstrates that `SyncVectorEnv`, `AsyncVectorEnv`, and custom (NumPy) vectorization exhibit environment- and hardware-dependent performance trade-offs, and that the `VectorEnv` abstraction allows users to switch between strategies without changing algorithm code. The benchmarks provide useful practical guidance.

## Weaknesses

### Fatal

None.

### Major

- **Core claims about streamlining and reproducibility are unsupported by evidence.** The abstract asserts that Gymnasium "significantly streamlines the process of developing and testing RL algorithms," "enables researchers to focus more on innovation," and "provides tools to ensure reproducibility and robustness" (lines 4–6). The only quantitative evaluation in the paper is the vectorization throughput benchmarks (Figures 1–2), which measure steps/second on Cartpole and Lunar Lander — a metric completely tangential to streamlining, development overhead, code complexity, interoperability, or reproducibility outcomes. No experiments, user studies, or even adoption statistics are provided that directly support these central claims. The paper's evidence does not match the magnitude of its stated contributions.

- **No systematic comparison with the predecessor (OpenAI Gym).** The paper states that Gymnasium "extends the Gym API" and introduces "new features" (Section 4), but it never provides a structured baseline comparison. For each claimed novel feature — termination/truncation separation, FuncEnv, algebraic spaces — the paper asserts novelty without a feature matrix, mapping of what existed in the last version of Gym versus what is new, or discussion of how Gym 0.26+ handled these concerns. A reader familiar with Gym cannot determine whether the differences are substantive or merely cosmetic reorganizations. (Note: the reviewer speculation that "termination/truncation was partially present in Gym 0.26+" is not verifiable from the paper and is excluded from this weakness; the weakness is the *absence* of a clear baseline, not any specific claim about what existed.)

- **No evaluation of the paper's own novel design contributions.** The FuncEnv (Section 4.1), termination/truncation distinction (Section 4.2), and algebraic spaces (Section 4.3) are described in detail but never empirically validated. Does the FuncEnv actually enable hardware acceleration (mentioned in passing in the summary, line 245)? Does the termination/truncation separation lead to measurably fewer bugs or faster development? Do algebraic spaces enable environments that were previously impossible or impractical to represent? No evidence is provided for any of these feature-level claims. The paper describes design decisions but never tests whether they achieve their intended effects.

### Minor

- **Vectorization benchmarks lack statistical rigor.** Figures 1–2 show performance comparisons across vectorization modes and hardware configurations, but no error bars, variance information, or indication of multiple runs is provided (confirmed: no mention of seeds, trials, or standard deviation anywhere in the paper). The comparison between MacBook Pro and Google Colab results is qualitative, relying on single hardware instances rather than controlled replication.

- **No limitations or scoping discussion.** The paper does not discuss what Gymnasium does not handle well, where the API might be constraining, or how its design choices trade off against alternatives like dm_env. Multi-agent support is implicitly deferred to PettingZoo and offline RL to Minari, but this scoping is never made explicit.

- **No adoption or community impact data.** As a library paper, evidence of ecosystem adoption (download counts, number of dependent projects, endorsed algorithms) would naturally strengthen the case for Gymnasium's value, but none is provided.

### Trivial

- The claim "accelerates the development of safe, socially beneficial artificial intelligence" in the introduction (line 22) is rhetorical and unsupported by anything in the paper.

## Nice-to-Haves

- A simple empirical comparison, even anecdotal, of implementing the same environment or training loop in Gymnasium vs. OpenAI Gym (or dm_env) would directly support the streamlining claim.
- A concrete worked example of the FuncEnv being used with an off-the-shelf algorithm would demonstrate the practical value of the POMDP-aligned API.
- A feature-comparison table mapping Gymnasium's novel features against the state of OpenAI Gym at the time of the fork would resolve the baseline ambiguity.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"termination/truncation was partially present in Gym 0.26+"** (Harsh Critic): This is an unsupported speculation about the predecessor's state. The paper claims these concepts were "not clearly separated" in Gym; the critic provides no evidence for the counterclaim. Removed per Hard Rules (speculative assertion depending on information not in the paper).
- **"PettingZoo 'builds on concepts from Gymnasium' — this is vague and unhelpful"** (Harsh Critic): A minor style opinion about a single sentence in the Related Work section. Not a substantive weakness. Removed per Filtering Discipline (formatting/style nitpick).
- **"The framing overpromises... reads as rhetoric"** (Harsh Critic): Subjective stylistic judgment without concrete anchor in a specific erroneous claim. Removed per Filtering Discipline.
- **"The introduction ends with 'accelerates the development of safe, socially beneficial AI' — this is unsupported"** (Harsh Critic): This claim is indeed unsupported, but it is a *trivial* rhetorical flourish, not a substantive weakness. Moved to Trivial.
- **"No baseline is provided... A reader familiar with Gym cannot assess whether Gymnasium's improvements are real or merely renaming existing functionality"** (Harsh Critic): The "merely renaming" speculation is removed; the structural point (no systematic comparison) is retained in Major weaknesses.
- **Various section-by-section subjective opinions** ("This section would benefit from concise API examples," "reads as an observation rather than a design justification"): These are presentation or taste preferences, not verified weaknesses. Relevant substantive kernels are retained in the Major/Minor sections.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no insight not already present in or directly derivable from the paper itself. The core tension is obvious: the paper describes a widely used library with genuine design merits but provides almost no evidence that its design decisions achieve the stated goals.

## Suggestions

1. **Tone down the claims or provide evidence for them.** Either remove "significantly streamlines" and "enables researchers to focus more on innovation" from the abstract, or add a simple experiment — e.g., implement the same algorithm in Gymnasium versus OpenAI Gym and compare code length, time to first working result, or bug frequency.

2. **Add a systematic baseline comparison.** Include a table mapping each feature described in Section 4 against the corresponding state of OpenAI Gym at the time of the fork. This would immediately clarify the incremental contribution.

3. **Provide at least one concrete use case for FuncEnv** showing it being used end-to-end with an actual algorithm, preferably with a hardware acceleration demonstration if that is claimed.

4. **Replace or supplement the vectorization benchmarks** with evidence more central to the paper's claims — e.g., a reproducibility case study or an interoperability demonstration across multiple training libraries (SB3, CleanRL, Tianshou).

5. **Add a limitations paragraph** explicitly scoping Gymnasium's API to single-agent, online RL and directing readers to PettingZoo, Minari, etc. for extended use cases.
