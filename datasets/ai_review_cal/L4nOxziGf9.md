- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes RAR (Rephrase, Augment, Reason), a zero-shot framework that addresses underspecification in VQA by: (1) extracting visually-grounded details from captions, rationales, and question entities, (2) generating rephrased question candidates using an LVLM's LLM component, and (3) selecting the best candidate via the LVLM's answer confidence as an unsupervised scoring function. The main empirical results (Table 1) show consistent absolute accuracy improvements across VQAv2 (+3.85%), A-OKVQA (+6.41%), and VizWiz (+7.94%) for three model families (BLIP-2, MiniGPT-4, LLaVA-1.5), with ablations validating the multi-source design.

## Strengths

1. **Consistent gains across multiple datasets and LVLM architectures** — Table 1 shows absolute improvements of +3.85% on VQAv2, +6.41% on A-OKVQA, and +7.94% on VizWiz, replicated across BLIP-2 (two sizes), MiniGPT-4 (two sizes), and LLaVA-1.5 (two sizes). The gains are not confined to a single model or benchmark.

2. **RAR questions are both easier to answer and easier to select than paraphrases** — Table 4 shows that RAR outperforms a Pegasus paraphrase baseline in the oracle setting (72.42% vs. 70.99% on VQAv2), and crucially the confidence-based selection works well for RAR (66.43%) while it *degrades* performance for paraphrases (62.91%, below the 62.58% baseline). This distinguishes RAR from mere lexical rewrites.

3. **Controlled ablation isolates each component's contribution** — Table 2 (ablations) shows that removing rationales (-2.71%), captions (-1.24%), or question entities (-1.39%) all hurt accuracy. Using image embeddings during fusion (-4.10%) or question likelihood as the selection score (-1.81%) also degrade performance. This validates the multi-source design empirically.

4. **Evidence that RAR leverages both the LLM and the image** — Table 5 (LLM-only analysis) shows RAR questions improve LLM-only accuracy (from 32.84% to 40.53% on VQAv2) while still maintaining a large gap when the image is added (67.28%), confirming the rephrasing complements rather than replaces visual information.

5. **Quantitative complexity increase confirms reduced underspecification** — Table 5 (complexity analysis) reports higher Average Dependency Distance (17.87→29.52 on VQAv2) and Idea Density (0.258→0.296), providing measurable evidence that RAR questions are syntactically and semantically more complex, i.e., less underspecified.

## Weaknesses

### Fatal
None.

### Major

1. **Confidence-based selection is unvalidated against a trivial baseline.** The paper's central selection mechanism—picking the candidate with the highest answer likelihood—is never compared against a random selection baseline over the same candidate set. The ablation shows answer-confidence scoring outperforms question-likelihood scoring (Table 2), but this still does not decompose how much of the reported gain comes from genuinely better candidates versus the selection function itself. A random-selection baseline over the RAR candidate set would directly address whether confidence adds value beyond simply generating better candidates. Without it, the contribution of the selection module is unclear. (Anchored in Table 1's main results vs. the unvalidated scoring function in §3.2.)

### Minor

1. **Complexity analysis is conducted on only 100 examples without significance tests.** The ADD/ID analysis (Table 5) uses 100 instances from the validation set. While the results are directionally clear, the small sample size and absence of statistical testing weaken the claim that the observed complexity increase is robust and representative. (§4.3, lines 327–328)

2. **The "asymmetric strength" analysis is only demonstrated for BLIP-2.** The LLM-only experiments in Table 5 (§4.4) are conducted only for BLIP-2. The paper motivates asymmetric strength as a general property of LVLMs in the introduction (footnote 1), but does not verify whether the same pattern holds for MiniGPT-4 or LLaVA-1.5. While this is a scope limitation rather than a flaw, it leaves the claim's generality partially unsubstantiated.

3. **NLI filtering is introduced but not analyzed.** The paper uses an off-the-shelf NLI model to discard candidates that contradict the original question (§3.1), but never reports how many candidates are discarded or whether filtering correlates with downstream accuracy. This is a minor gap in the method description.

### Trivial
None.

## Nice-to-Haves

- **Testing CoT as a baseline** would strengthen the positioning against prior work, though the paper provides a reasoned argument (citing Wei et al. 2022) that CoT benefits emerge at 100B+ parameters, which none of the models used here reach.
- **Statistical significance tests** (e.g., matched-pairs bootstrap) on the main results would strengthen confidence in the reported improvements, though the consistent trend across 5 model variants and 3 datasets is already compelling.
- **A "caption + original question" baseline in the full LVLM setting** (rather than the LLM-only setting in Table 5, Row 5) would further isolate the role of rephrasing versus simply appending visual text.

## Removed Points

- **"Oracle results overstate the method's potential"** — Removed. The paper explicitly labels oracle results as "upper-bound" (lines 70, 168, 234) and clearly reports both actual and oracle gains. The gap between them is a natural feature of any oracle analysis, not a misrepresentation.
- **"CoT absent as a major weakness"** — Demoted to Nice-to-Have. The paper provides a citation-supported argument about CoT requiring 100B+ parameters (Wei et al. 2022) and notes Flan-T5 models do not benefit from CoT. The reasoning is present even if an experiment is not.
- **"Rephrasing using only LLM (no image grounding)"** — Removed. This is what the Pegasus paraphrase baseline tests in Table 4 — a non-visual rephrasing baseline is already included.
- **General comments about missing related work** — Removed per instructions (cannot verify existence of external works).
- **Formatting/style nitpicks and reproducibility concerns about hyperparameters** — Removed per hard rules.

## Novel Insights

The reviews surface an interesting tension: the paper's claimed contributions are actually two-fold (candidate generation with visual grounding + confidence-based selection), but the experimental design conflates them. The paraphrasing comparison (Table 4) cleverly isolates the *quality* of RAR candidates (they are both more answerable and more selectable than paraphrases), but it does not isolate the *quality of the selection function* itself. A random-selection ablation — where the field standard would be a simple "pick any candidate" baseline — would cleanly decompose the pipeline. The paper's strongest empirical contribution may actually be the demonstration that visually-grounded candidate generation (Stage I) is the primary driver of gains, with the selection function playing a secondary (still helpful but not independently validated) role.

## Suggestions

1. **Add a random-selection baseline** over the same RAR candidate set (choose a random candidate instead of confidence-based selection) to decompose the contributions of candidate generation vs. selection. This directly addresses the major weakness.
2. **Repeat the LLM-only analysis (Table 5) for at least one additional model** (e.g., MiniGPT-4 7B) to strengthen the generality of the asymmetric strength claim.
3. **Report NLI filter statistics**: how many candidates are discarded on average per question, and a small analysis of whether discarded candidates would have been poor choices.
4. **Expand the complexity analysis to a larger sample** (e.g., 500–1000 examples) and add a simple significance test to support the underspecification reduction claim.
