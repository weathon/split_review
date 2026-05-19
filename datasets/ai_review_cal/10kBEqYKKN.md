- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3
Now I have all the information I need. Let me construct the consolidated review.

---

## Summary

This paper investigates how zero-shot prompt formulations affect the geometric properties of LLMs' latent representations. It studies how IsoScore (a measure of isotropic variance distribution) varies across layers for different prompts, models, and sentiment-analysis datasets, and applies KMeans clustering to EOS-token representations to see whether prompts group by geometric rather than semantic similarity. The paper reports that prompts produce measurable differences in representation geometry, that these effects are model-family dependent, and that clustering groups prompts in ways that do not align with their natural-language similarities.

## Strengths

- **Systematic multi-family, multi-dataset comparison.** The paper evaluates four model families (Gemma, Phi, Zephyr, Bloomz) on three binary sentiment datasets (Rotten Tomatoes, IMDB, YELP), establishing that isotropy evolution patterns are model-family dependent and not merely a dataset artifact (Figure 1, Table 2). This breadth gives the analysis more weight than a single-model study.

- **First targeted exploration of prompt-conditioned isotropy in LLMs.** Prior work on isotropy (Ethayarajh 2019; Cai et al. 2021) studied representation geometry in general; this paper specifically investigates how *prompt variation* within a zero-shot setting changes layer-wise isotropy — a narrower and less-explored question. Table 3 reports non-trivial relative variation in IsoScore across prompts (std/mean percentages), suggesting prompt formulation has a measurable effect even if absolute values are small.

- **Clustering analysis reveals non-semantic grouping patterns.** Table 4 shows that semantically close prompts (e.g., different variants of "Movie Expressed Sentiment") do not consistently cluster together, while semantically less-related pairs sometimes do (~20% co-grouping). This result, though limited by missing prompt specifications, supports the paper's claim that models can attend to geometric features over surface-level semantics.

- **Stable layer-wise clustering signals structure beyond noise.** Figure 4 reports high Random Index Scores between consecutive layers after majority voting, indicating that the clustering assignments are consistent across model depth rather than being layer-specific noise. This strengthens the case that the geometric features captured by KMeans are non-trivial.

## Weaknesses

### Major

- **Experimental methodology is critically underspecified.** The paper never describes how model outputs are mapped to binary labels (used to color prompts in Figure 2), nor does it specify generation parameters (temperature, max tokens, stop conditions). The full set of prompts tested is not listed — only four named prompts appear in Table 4, and the prompt-construction process ("default templates duplicated with minor modifications") is too vague to reproduce. The paper even cuts off the in-text example ("for instance :") due to a missing figure reference. This is a structural reproducibility gap: a reader cannot verify the experimental setup or evaluate whether the accuracy-based coloring in Figure 2 is methodologically sound. (Relevant lines: §4.3, line 115; §5.1, line 143; Figure 2 caption.)

- **No statistical tests or baselines on any comparison.** All claims about IsoScore differences between prompts, clustering quality, and prompt grouping are based on qualitative visual inspection or descriptive statistics. The Random Index Score is reported without any chance-level baseline (what RIS would random assignments produce?), IsoScore differences across prompts are not tested for significance, and the visual claim that "bad prompts tend to destabilize internal representations" (Figure 2) is unsupported by any quantitative comparison. The paper would be substantially strengthened by even a simple permutation test or bootstrapped confidence intervals. (Relevant: §5.1 entire, §5.2 entire.)

- **Internal contradiction: Bloomz used in all results despite being "only for prototyping."** Section 4.1 states that Bloomz "is only used for prototyping purposes" due to data contamination concerns, yet Bloomz models appear in every main figure (Figure 1, Figure 2, Figure 3, likely Figure 4) and are analytically compared to other families (e.g., "the evolution of the isoscore is smoother for the Bloomz family," line 148). This undermines the paper's methodological coherence — either the model is valid for analysis or it is excluded. (Relevant: §4.1, line 80; §5.1 passim.)

- **The central evidence rests on IsoScore values near zero without addressing the implications.** The paper reports IsoScore values in the range 0–0.006 (at most 0.6% of dimensions used), calls this "expected" (line 133), and then uses these values to claim prompt-induced geometric modification. While the relative variation across prompts (Table 3) may be non-trivial, the absolute scale is so close to floor that noise sensitivity and the interpretability of percentage-of-mean normalization are serious concerns. The paper does not address whether the observed differences exceed what would arise from sampling noise or numerical precision. (Relevant: §5.1, lines 133–143; Table 3.)

- **Tension between the paper's own acknowledgment and its claims.** The paper states that "isoscore is not a relevant measure to analyze the efficiency of prompts" (line 143) and later concedes in the conclusion that "while this may seem like a reasonable and expected statement" (line 190). This self-awareness partially mitigates overclaiming, but it also creates uncertainty about what exactly the paper's evidence demonstrates — if the primary metric is acknowledged as not relevant for performance analysis and the conclusion is acknowledged as "expected," the concrete contribution becomes unclear.

### Minor

- **No ablation or control experiments.** The paper does not compare against trivial baselines that would strengthen the causal interpretation of the results: e.g., replacing prompts with random non-informative text, comparing to untrained (random) model layers, or testing whether the observed geometric differences between prompts exceed those between random splits of the same prompt. Adding such controls would substantially increase confidence that the observed effects are specific to prompt formulation.

- **The justification for extracting only the EOS token representation is asserted without support.** The paper claims "only the last generated representation is able to capture all contextual information" (line 50) without citation or argument, and the meaning of "EOS token" in a zero-shot (no generation) setting is ambiguous. While focusing on a single token is a reasonable scoping choice, the rationale should be justified, and the scope limitation should be acknowledged.

- **Prompt grouping analysis lacks semantic ground truth for "expected" behavior.** Table 4 labels certain groupings as "unexpected" or "counter-intuitive," but the paper never formalizes what the expected grouping would be (e.g., by human judgment, by embedding similarity in a reference encoder, or by a simple baseline). Without this, the reader cannot assess whether the reported grouping pattern is genuinely surprising or merely noisy.

- **Missing analysis relating geometric properties to actual content.** The paper collects prompt-conditioned representations for positive and negative examples but never analyzes whether geometry differs by sentiment class. This is a missed opportunity to connect the geometric analysis to the task structure.

### Trivial

- The paper has minor formatting inconsistencies (e.g., "isoscore" vs. "IsoScore," section numbering style).
- The in-text example of a prompt template cuts off abruptly (line 115–118, probably a figure reference lost during parsing).

## Nice-to-Haves

- Reporting confidence intervals or bootstrapped estimates for IsoScore values would address concerns about the near-zero absolute scale.
- A simple permutation baseline for the clustering RIS (e.g., randomly shuffling prompt labels) would make the "good RIS" claim quantitative rather than qualitative.
- Including a table of the exact prompt templates used would fix the most critical reproducibility gap.
- The accuracy data used to color Figure 2 could be analyzed directly (e.g., correlation between IsoScore and accuracy) instead of serving only as a visual cue.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The paper's claim that 'no works have studied the impact of zero-shot prompting approaches on the geometry of latent representation' is overstated."** — The paper's claim is about the *specific combination* of zero-shot prompting *and* representation geometry. Prior work on isotropy (Ethayarajh, Cai) studied general representations, not prompt-conditioned variation. The claim is defensibly narrow and removing it does not change the paper's standing. Removing rather than litigating, in line with instructions to avoid contesting novelty claims without external verification.
- **"No discussion of computational cost or limitations of the models used."** — Not required for an empirical analysis paper of this type; added cost information would not strengthen or weaken the core claims.
- **"The paper conflates isotropy with dimensional usage."** — IsoScore is explicitly designed to measure isotropy via dimensional variance uniformity. The paper's framing is consistent with the metric's definition.
- **"The paper never formulates a prediction about what relationship should hold [between isotropy and performance]."** — This is a stated goal of the paper (RQ1: exploring whether there is a relationship), not a flaw. Exploratory studies do not require a priori predictions.

## Novel Insights

None beyond the paper's own contributions. The main insight offered by the reviewers is methodological: the near-zero absolute IsoScore values, combined with the use of percentage-of-mean normalization, create an evidence base that is more fragile than the paper's narrative suggests. This is a useful caution but does not constitute a new finding about the subject matter.

## Suggestions

1. **Fully specify the experimental setup.** List all prompt templates, report generation/decoding parameters, and describe the label-extraction pipeline used to compute accuracy scores. This is the single highest-impact fix for the paper's credibility.
2. **Add statistical grounding.** Report confidence intervals or bootstrap estimates for IsoScore; add a chance-level baseline for the Random Index Score (e.g., permuted labels); test whether IsoScore differences across prompts exceed what noise would produce.
3. **Resolve the Bloomz contradiction.** Either exclude Bloomz from the main results if data contamination is a genuine concern, or justify its inclusion and remove the "prototyping only" statement.
4. **Add control experiments.** Compare prompt-conditioned representations to representations from semantically empty templates or random token sequences; compare clustering results to a random-clustering baseline.
5. **Clarify the "EOS token" extraction.** Explain what "EOS" means in a zero-shot setting with no generation, and justify (or qualify) the exclusive focus on the final token's representation.
