- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 6, 6, 5
Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

---

## Summary

This paper proposes CIPHER, a communication protocol for multiagent debate among LLMs that replaces token-level sampling with a weighted average of token embeddings. The motivation is that standard token sampling discards the model's full belief distribution over the vocabulary. CIPHER generates convex combinations of token embeddings weighted by the softmax probabilities at each autoregressive step, then feeds these directly as input to the other LLM. The method is evaluated across five reasoning tasks (GSM8K, Arithmetic, three MMLU subsets) and several open-source LLMs (LLaMA-65B, LLaMA2-70B, Falcon-40B-Instruct, MPT-30B, WizardMath-70B), reporting 0.5–5.0% absolute accuracy improvements over natural language debate (NLD) without any model weight modification.

## Strengths

- **Consistent empirical gains across models and tasks.** The paper reports that CIPHER outperforms natural language debate across all five reasoning tasks, with 1.0–5.0% improvement for the LLaMA family (Table 1) and 0.5–3.5% for other open-source models on GSM8K (Fig. 3). The consistency across 5 datasets and 5+ model families provides convergent evidence that the method's advantage is not dataset- or model-specific.

- **Ablation study directly supports the claimed mechanism.** The partial CIPHER experiment (Fig. 7) shows that applying CIPHER generation only at positions where the model exhibits high uncertainty (measured by entropy or 1−max probability) closely matches the performance of full CIPHER, while the reversed variants (CIPHER only at certain positions) perform poorly. This causally links CIPHER's advantage to information retention at uncertain positions, which is exactly the paper's central thesis.

- **Temperature sensitivity analysis reveals a distinct advantage.** The 2D contour plots (Fig. 6) show that CIPHER optimally pairs a low-temperature agent with a high-temperature agent, while NLD performs best with both agents at low temperatures. This provides quantitative evidence that embedding-based communication productively leverages diverse temperature agents—a qualitative difference from natural language debate, not just a quantitative one.

- **No model retraining or weight modification.** CIPHER is implemented purely through changes to the generation and input protocol (Algorithm 1, Equations 3–4), with no fine-tuning or weight access beyond what is required for standard inference. This lowers the barrier for adoption.

- **Cross-model debates with different embedding spaces.** The paper demonstrates a mapping strategy (Section 4.2) for debates between LLaMA-65B and LLaMA2-70B that uses the receiver's embedding space, showing applicability beyond identical-model settings.

## Weaknesses

### Fatal
None.

### Major

- **Small evaluation sets with no statistical rigor.** For the three larger datasets (GSM8K, Arithmetic, Professional Psychology), the paper evaluates on only 200 test questions. A 1% difference corresponds to 2 questions out of 200. The reported improvements range from 0.5% to 5.0%, but no confidence intervals, standard deviations, or significance tests are reported anywhere in the paper. The two MMLU subsets (Formal Logic, High School Math) are likely evaluated on full test sets of ~100 examples each, which is even smaller. The paper does note that baseline methods exhibit 0.5–3.0% variance due to token sampling, but does not quantify the variance of the central comparison. Given that the headline quantitative claims are the paper's primary evidence for CIPHER's superiority, the lack of any statistical characterization is a significant weakness. The results are suggestive and consistent, but the reader cannot assess whether the smaller reported advantages (e.g., 0.5–1.0%) are within the noise of the estimation procedure.

### Minor

- **Ambiguity in the experimental design for generating multiple CIPHER responses.** The paper states: "We evaluate debates based on the final responses of the agent with a lower temperature, resulting in five responses per debate. For fair comparisons, our self-consistency baselines (labeled as Major@5) also use five responses." However, the paper also describes CIPHER's embedding generation as deterministic ("CIPHER's deterministic embedding generation ensures consistent outputs"). It is unclear how five distinct responses are obtained per debate under deterministic generation — whether through different temperature pairs, different initial seeds, multiple runs, or another mechanism. Without clarification, the fairness of the comparison with Major@5 (which naturally produces 5 different samples) is difficult to assess.

- **No discussion of computational cost.** The paper does not compare the computational cost (e.g., number of forward passes, token-generation overhead) between CIPHER and NLD. While the same architecture is used, CIPHER's weighted embedding generation and nearest-neighbor decoding may have different computational characteristics than token sampling. A brief note on this would strengthen the paper.

- **Missing single-agent embedding baseline.** The paper would benefit from a baseline where CIPHER is used in a self-consistency setup (a single model generating multiple embedding sequences, then decoded and aggregated) to isolate whether the gains come from the embedding representation itself or from the multiagent debate interaction. The partial CIPHER ablation partially addresses this by isolating the mechanism, but a single-agent embedding consistency baseline would further clarify the source of improvement.

### Trivial
None.

## Nice-to-Haves

- **Analysis of out-of-distribution embedding effects.** CIPHER generates convex combinations of token embeddings that do not correspond to any real token. The paper acknowledges this ("CIPHER-generated semantic embeddings approximate a token embedding, but do not precisely match it") but provides no analysis of how LLM internal representations or calibration are affected. While the ablation study and empirical results suggest this is not a practical problem, a brief analysis (e.g., monitoring logit entropy or calibration under distribution shift) would strengthen the understanding of why the method works.

- **A single-agent CIPHER self-consistency baseline** (as described above) would help disentangle the debate benefit from the embedding-representation benefit.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Positional embedding concern** (Harsh Critic, Section-by-Section Notes). The critic asks how positional information is handled when CIPHER embeddings are concatenated with prompt embeddings. In standard transformer architectures, all input token embeddings (including those produced by CIPHER at each position) receive positional encodings automatically based on their position in the sequence. This is a routine implementation detail, not an undiscussed gap. → Removed (implementation nitpick that is straightforward from the description).

- **Closed-source model limitation** (Harsh Critic, "Missing Parts and Places to Improve"). The critic states that CIPHER requires model access at the embedding level, which excludes closed-source API models. The paper's scope is explicitly open-source models for which this access is available, and the paper states "we anticipate that CIPHER will inspire further exploration" — it does not claim to solve closed-source debate. → Removed (scope-appropriate; the paper is evaluated on its own terms).

- **OOD analysis as a "significant weakness"** (Harsh Critic, Critical Issue #3). The critic frames the lack of deeper analysis of out-of-distribution embeddings as a significant weakness. However, the paper provides an ablation study (partial CIPHER) that directly investigates the mechanism and shows the method works as intended. The empirical results demonstrate the method functions correctly. The request for deeper theoretical analysis is reasonable as future work but does not threaten the paper's core empirical contribution. → Demoted to Nice-to-Have (not a core weakness).

- **"Overstated novelty" claim** (Harsh Critic, Introduction & Related Work notes). The critic says "the core idea of averaging embeddings is straightforward once the problem is framed." This is a subjective assessment of novelty that does not identify an actual flaw in the paper. The contribution lies in identifying the problem (information loss from sampling) and demonstrating that the straightforward fix works consistently across models and tasks. → Removed (subjective opinion about novelty level, not a verifiable weakness).

## Novel Insights

The harsh critic and strength finder together surface one insight that goes beyond the paper's own claims: the paper is stronger on mechanistic evidence (partial CIPHER ablation, temperature contour plots) than on raw benchmark performance. The ablation and temperature analysis convincingly demonstrate *why* embedding communication helps (information retention at uncertain positions, productive use of diverse temperatures), and this mechanistic evidence is arguably more compelling than the absolute accuracy numbers on 200-sample test sets. A reader should weigh the ablation and temperature analysis more heavily than the point estimates in the main tables.

## Suggestions

1. **Run the main comparisons on the full GSM8K test set (1,319 examples) or report confidence intervals** on the current 200-sample sets. Bootstrap confidence intervals or error bars from multiple runs of the stochastic baselines would let readers assess whether the reported advantages exceed the noise floor.
2. **Clarify how "five responses per debate" are generated for CIPHER.** If this involves running the debate multiple times with different configurations, specify what varies. If it is a single deterministic run, explain what "five responses" means.
3. **Add a brief compute comparison** noting the number of forward passes required for CIPHER vs. NLD for the same debate setup.
4. **Include a single-agent variant** where CIPHER's expected embeddings are used in a self-consistency setup (multiple independent embedding sequences aggregated via decoding and voting) to disentangle the debate effect from the embedding effect.
