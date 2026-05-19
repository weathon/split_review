- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5
Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper adapts statistical-physics methods (f-divergence-based dissimilarity measures) to detect abrupt changes in LLM output distributions across three types of control parameters: an integer in the prompt, the generation temperature, and the training epoch. Applied to Pythia, Mistral, and Llama3 models, the method produces several interesting observations — a tokenizer boundary at T≈2021, two distinct temperature-induced transitions partitioning behavior into three phases (frozen/coherent/disordered), and epoch-level coincidences between weight and output changes. The core method is a straightforward adaptation of existing techniques, and the paper's main contribution lies in the demonstration and the observations themselves.

## Strengths

- **Reliably detects a known behavioral transition where it should.** For the prompt "T is larger than 42. True or False?", all dissimilarity measures peak sharply at T=42 for instruction-tuned models and are flat for base models (Figure 1, Sec. 4.1). This validates that the method captures genuine distributional changes, not spurious noise.

- **Discovers a three-phase structure in temperature behavior that was previously unmapped.** The linear dissimilarity exhibits two distinct peaks near T≈0.02 and T≈0.5, partitioning LLM behavior into "frozen" (near-deterministic), "coherent" (sensible and diverse), and "disordered" (random) phases (Figure 2, Sec. 4.2). Prior work had speculated about a higher-temperature transition; this paper provides direct evidence.

- **Applicable across three fundamentally different control parameters without modification.** The same dissimilarity measure detects transitions when the parameter is part of the prompt (Sec. 4.1), a generation hyperparameter (Sec. 4.2), or a training epoch (Sec. 4.3). This versatility — running on outputs alone, without task-specific metrics or weight access — is a genuine practical advantage over existing approaches.

- **Incidental discovery of a tokenizer boundary.** The method reveals a sharp transition at T≈2021 in Pythia models that the authors trace to a change in tokenizer encoding behavior (Figure 1b, Sec. 4.1). This demonstrates the method's potential to surface artifacts that would not be found with task-specific evaluations.

## Weaknesses

### Fatal
None.

### Major

- **The "phase transition" framing overreaches for several key demonstrations.** The paper defines the term broadly ("a sudden shift in the qualitative behavior"), but the title and abstract evoke the much stronger physics concept of fundamental changes in system organization (order/disorder, symmetry breaking). Three points of tension: (1) the integer-ordering transition (T=42) is a simple classifier decision boundary, not a change in model organization; (2) the high-temperature peak in Sec. 4.2 is itself acknowledged as "perhaps better described as a crossover rather than a phase transition" (line 169); (3) many peaks in the epoch analysis are single-point outliers that the authors themselves say "do not mark transitions between two macroscopic phases of behavior" (line 193). These explicit concessions in the text contradict the paper's overarching "phase transition" rhetoric, creating a mismatch between the marketing and the evidence.

- **The heat capacity analysis is used as validation but its thermodynamic interpretation is acknowledged to be invalid.** The paper defines energy as E(x) = −log P(x|T=1) and computes C(T) = ∂E[E(x)]/∂T, then shows peaks aligning with the dissimilarity peaks. The authors correctly note that "the text outputs are not truly sampled from a Boltzmann distribution governed by the total energy" (line 167). However, the paper still lists "an LLM's 'heat capacity' … can be negative" as a specific finding (line 31) and uses the alignment in Figure 2 as corroborating evidence. Since the sampling distribution is not a Boltzmann distribution over this energy, the quantity has no thermodynamic meaning as heat capacity; the alignment is interesting but does not independently validate the dissimilarity peaks. This is a presentational overreach even with the caveat included.

### Minor

- **The training epoch analysis is exploratory and stops short of establishing robust claims.** The most concrete observation — output peaks near epoch 80K potentially aligning with rapid weight changes in layer 4 — relies entirely on visual inspection with no statistical test of alignment or causal mechanism. The small-L peaks are honestly identified as outliers (line 193), which is transparent but also means the evidence for meaningful training-phase transitions is thin. The claim that "different prompts result in different transition times" (line 197) is supported by only seven short prompts, all generic, making it suggestive but not generalizable.

- **Limited robustness characterization of the temperature phase boundaries.** The paper notes qualitatively that "many distinct prompts lead to a transition at T≈1 and/or T≪1" (line 171) but provides no systematic analysis of how the peak locations or the three-phase structure vary across prompts, model sizes, output lengths, or numbers of generated tokens. The two temperature peaks are observed for a single prompt with a single model; generalizability is asserted but not demonstrated.

- **No principled criterion for choosing the segment length L.** The paper shows that L strongly affects results (Figures 1b, 5) and discusses trade-offs qualitatively, but provides no guidance (cross-validation, sensitivity analysis, or heuristic) for selecting L in a new setting. This limits the method's turnkey usability.

### Trivial

- The footnote on line 89 (the claim that any g-dissimilarity with g(1/2)=0 reduces to Fisher information) is truncated/formatted incoherently in the extracted text. If this is a submission artifact rather than a parser issue, it should be completed.

## Nice-to-Haves

- A multi-parameter demonstration (e.g., temperature × prompt integer) would strengthen the claim of generality.
- A computational cost analysis (number of samples × model calls needed for reliable detection) would help practitioners assess the method's practical utility.
- More quantitative characterization of the three temperature phases (e.g., measuring output entropy, perplexity, or semantic coherence within each region) would make the "frozen/coherent/disordered" labeling testable rather than intuitive.

## Removed Points

Points flagged for removal; treat them with caution.

- *"The heat capacity analysis is conceptually invalid and fatal"* — **Removed** because the paper explicitly acknowledges the sampling mismatch (line 167). The authors do not claim rigorous thermodynamics; the analysis is presented as an analogy. Calling it "fatal" misrepresents the paper's own disclosure.

- *"No attempt to characterize the three phases"* — **Removed** because the paper does characterize them qualitatively (line 154: "frozen … unfrozen and sensible … random"). The characterization is intuitive rather than quantitative, which is a limitation but not an absence.

- *"Training epoch analysis lacks causal evidence"* — **Removed** because the paper does not claim causality. It says "potentially related" (line 191) and "it remains an open question" (line 193). The critic's demands exceed what the paper asserts.

- *"Missing critical comparison with methods that identify phase transitions (e.g., scaling tests)"* — **Removed** per instruction: missing related works cannot be flagged without external confirmation of their existence.

- *"Statistical significance across prompts" and "power analyses"* — **Removed** as generic methodological demands that do not anchor to a specific error in the paper. The paper does report error bars throughout; the critic's request for bootstrapping is a preference rather than a demonstrated flaw.

- *"Integer ordering is a trivial decision boundary, not a new phase"* — **Weakened to major weakness** on framing mismatch, rather than removed entirely, because the paper itself uses this example as validation — it's a demonstration that the method works, not claimed as a discovery of a new phase. However, the paper's persistent "phase transition" framing makes even validation examples sound like discoveries, which is the real problem.

## Novel Insights

The two-reviewer synthesis surfaces a tension that neither reviewer fully articulated: the paper's method and its rhetoric operate on different levels. The dissimilarity-based detection is a genuinely useful tool for surfacing distributional discontinuities — the tokenizer boundary at T≈2021 is a clean example of an unknown-unknown that the method finds automatically. But the paper systematically labels every discontinuity a "phase transition," which conflates three distinct phenomena: (1) classifier-style decision boundaries (integer ordering), (2) genuine changes in generative diversity (temperature), and (3) training dynamics that may or may not correspond to qualitative reorganizations (epoch analysis). The most valuable unforced contribution is the three-phase temperature structure; the most strained one is the heat capacity analysis. A version that reframed the contribution around "automated detection of distributional discontinuities" and reserved stronger language for cases where the qualitative nature of outputs actually changes would be more credible and better highlight what is genuinely novel.

## Suggestions

1. **Reframe the paper's central contribution** from "detecting phase transitions" to "detecting abrupt distributional changes." This is a more defensible characterization that does not require disclaimers for every example and allows the temperature three-phase finding to speak for itself.

2. **Relegate the heat capacity analysis** to a supplementary curiosity or remove it. Its role as validation in Figure 2 is undercut by the acknowledged sampling mismatch; keeping it as an aside observation ("interestingly, this quantity can be negative") would be more honest than presenting it alongside the dissimilarity as though both were independent physical measurements.

3. **Replace the qualitative phase labels for temperature** with quantitative metrics measured within each regime — e.g., output entropy, token-type diversity, perplexity gap from the training distribution, or semantic coherence scores. This would turn the intuitive "frozen/coherent/disordered" naming into a testable claim.

4. **Add a systematic prompt and model robustness study** for the temperature experiment: vary prompts (at least 10–20 covering different domains), model sizes, and output lengths, and report the distribution of the two peak locations.

5. **For the epoch analysis, focus on robust multi-epoch peaks** (L=6 or higher) where the large-L averaging suppresses outliers, and test whether the remaining peaks align with known training events (learning rate schedule changes, data shard boundaries, loss plateaus). The outlier discussion is transparent but reduces what can be concluded.
