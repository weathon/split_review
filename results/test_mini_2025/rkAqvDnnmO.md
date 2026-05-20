Now I have a solid calibration base. Let me synthesize the final review.

## Summary
The paper proposes SimE, a simple and efficient class-incremental learning framework that combines a frozen CLIP vision encoder with lightweight adapter modules (AdaptFormer / Multi-Adapter) and a prototype-based classifier. The key claims are: (1) parameter-efficient IL with "only thousands of parameters," (2) competitive or superior accuracy without a memory bank, and (3) a finding that more within-block adapter connections do not always improve IL performance. The paper also includes a systematic study of CLIP backbone sizes and pre-training datasets.

## Strengths

1. **Strong accuracy with very few trainable parameters.** Table 1 shows SimE achieves 91.66% Avg on CIFAR-100 (10 steps), outperforming ZSCL (85.94%) which requires full-model finetuning (~140M params). SimE uses ~1.19M trainable parameters—roughly two orders of magnitude fewer than full-finetuning baselines. This is a genuine efficiency-accuracy tradeoff win.

2. **Rehearsal-free operation with competitive results.** SimE uses only prototypes (class-mean features) and a frozen encoder after the first task, requiring no storage of past images. It outperforms replay-based methods like CoOp and Continual-CLIP while using a memory bank size near 100 (prototype vectors only) versus 1000–2000 stored samples for those baselines.

3. **Useful systematic investigation of CLIP components.** Tables 3 and 4 provide a clean empirical study of how different CLIP pre-training datasets (WIT-400M, LAION-400M, LAION-2B, DataComp-1B, CommonPool-1B) and backbone sizes (ViT-B/16, B/32, L/14, L/14-336px) affect CIL performance. Practitioners can directly use these results for model selection.

## Weaknesses

### Fatal
None.

### Major

1. **Persistent, factual misrepresentation of parameter count.** The paper repeatedly claims SimE uses *"only thousands of parameters"* (Abstract, line 15; Section 4.2, line 232; Conclusion, line 355). **This is false.** Table 2 shows the smallest adapter configuration (Adapt-MLP only) uses **1.19 million** trainable parameters. Even the most aggressively bottlenecked configuration in Figure 4(d) uses ~0.5M. "Thousands" implies 1,000–9,999; 1.19M is two orders of magnitude larger. The core argument (parameter efficiency vs. 140M ZSCL) is still valid—1.19M vs 140M is a >100× reduction—so this exaggeration is unnecessary. But a reader who checks Table 2 will find the paper's own numbers contradict its headline claim. This must be corrected.

2. **Limited evaluation scope and lack of statistical rigor.** Experiments are conducted on only two datasets (CIFAR-100, TinyImageNet). No standard deviations, confidence intervals, or multi-seed results are reported anywhere. Given that the claimed phenomenon (Tables 2, rows showing ~0.5% differences between adapter configurations) relies on differences smaller than typical run-to-run variation in CL experiments, the absence of variance reporting makes it impossible to assess whether the observed trends are reliable. The paper should report results over at least 3–5 seeds.

### Minor

1. **Ambiguous framing of the "phenomenon" about within-block adapters.** The paper states that "within transformer blocks, adding more adaptive connections in smaller incremental steps does not enhance" IL ability. However, Table 2 shows that on 50-step settings (smaller per-step increment, 2 classes/step), more adapters *improve* Avg accuracy (84.16 → 85.00 from simplest to most complex configuration). On 10-step settings (larger per-step increment, 10 classes/step), more adapters slightly *hurt* (85.94 → 85.54). The verbal description is ambiguous: it is not clear whether "smaller incremental steps" refers to settings with fewer total steps (10 steps) or settings where each step adds fewer classes (50 steps). The data support the former reading, but the phrasing is easily misinterpreted. This needs to be clarified.

2. **Table 2 parameter count inconsistencies.** Rows with the same checkmark pattern show different parameter counts without explanation. For example, row 3 (✓ ✓ ✗) lists 1.19M while row 5 (✓ ✓ ✗) lists 2.38M. Since the table header provides only three adapter-type columns, the reader cannot tell what differs between these rows. The table likely also varies the bottleneck dimension or the number of blocks with adapters, but this is not stated. This makes the ablation difficult to interpret.

3. **Main results (Table 1) do not specify the adapter configuration used.** The SimE row in Table 1 reports top-line accuracy but does not state which adapter variant (Adapt-MLP only? Multi-Adapter with which sub-modules?) or bottleneck dimension was used. Given Table 2 shows several configurations with similar but non-identical results, the paper must specify what was actually evaluated for the headline numbers.

4. **Uncited baseline in Table 1.** The method "Fren-time" appears in Table 1 and Figure 3 without any citation or description in the main text. Readers cannot tell what this baseline is or whether it is a fair comparison.

5. **Figure 4 uses approximate values mixed with exact results.** The embedded tables in Figure 4 report approximate numbers (e.g., "~65", "~75", "~80") while the main tables use exact values. These approximate numbers occasionally conflict with exact numbers elsewhere (e.g., LwF accuracy differs between the Figure 4(a) table and Table 1). The figure should either be replaced with proper bar charts or exact numbers.

### Trivial
- "Fren-time" baseline not cited — should be referenced.
- The term "Fren-time" itself appears without explanation; if this is a method from another paper, cite it.

## Nice-to-Haves
- Report results with multiple random seeds and include standard deviations.
- Add a brief discussion comparing against prompt-based CIL methods that also use frozen pre-trained ViTs (e.g., L2P-style methods) to contextualize the adapter approach relative to other parameter-efficient strategies.
- Consider evaluating on additional datasets (e.g., ImageNet-R, CUB-200) to broaden the empirical support.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **Missing L2P/DualPrompt/CODA-Prompt baselines** — Per policy, I cannot verify the existence or non-existence of specific papers not cited in the manuscript. Removed per rule: "DO NOT mention missing related works, as you do not have external sources to confirm their existence and could be making things up."

2. **"The method's individual components are not novel" (general assessment)** — This is a sweeping claim not tied to a specific sentence, equation, or table in the paper. The harsh critic raised it as a general observation rather than a concrete weakness. The paper does claim novelty in the Multi-Adapter design and the observed phenomenon, and Table 2 provides the supporting data. Removed as not a specific, verifiable weakness.

3. **"CoOP memory bank claim is misleading"** — The paper states CoOP "requires a memory bank of size 1000." Whether this is an accurate characterization of CoOp depends on the specific variant being referenced, and this nuanced discussion is outside the paper's scope for the final review. Removed as it does not directly affect evaluation of SimE's contributions.

4. **Strength Finder's claim about "10,000× parameter reduction"** — The Strength Finder's framing uses the erroneous "thousands" number from the abstract. Since the paper itself reports 1.19M parameters, not 1,000–9,999, the strength is re-framed above as "roughly two orders of magnitude fewer" rather than "10,000×," which would have been based on the incorrect "thousands" figure. The corrected framing is retained in Strengths.

5. **"Orders-of-magnitude parameter efficiency"** — Reframed above to use the actual numbers (1.19M vs 140M ~ 118×, not the inflated >10,000× from the erroneous "thousands" claim). The corrected version is in Strengths.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a genuinely new observation about the paper or its approach that the paper itself does not already make.

## Suggestions
1. **Correct the parameter count claims throughout.** Replace "thousands" with "approximately 1 million" or "under 2 million." The efficiency story (1.19M vs 140M for ZSCL) is still very strong without exaggeration.

2. **Specify the default adapter configuration for all main results.** Clarify which variant from Table 2 was used in Table 1 and Figures 3–4, and report the bottleneck dimension.

3. **Resolve the Table 2 ambiguity.** Add a column for bottleneck dimension or number of adapter-equipped blocks to explain why identical checkmark patterns yield different parameter counts.

4. **Clarify the phenomenon description.** Rewrite the claim to precisely match the data: e.g., "For coarse-grained incremental steps (10 steps, 10 classes each), adding more within-block adapters does not improve accuracy. For fine-grained incremental steps (50 steps, 2 classes each), more adapters provide a modest improvement."

5. **Report results with at least 3 random seeds and include standard deviations,** especially for Table 2 where the performance differences between configurations are <1%.

## Score and Decision

**Calibration protocol:**

*Round 1 (bracketing):* Searched for CLIP+adapter+continual learning papers in score bands (<3.5, 3.5–7.5, >7.5). Weak-band anchors scored 2.3–3.0 (withdrawn papers with severe flaws). Middle-band anchors included C-CLIP (6.5, accepted poster), MetaAdapter (5.4, rejected), SimpleCIL/APER (4.75, withdrawn), TIPS (4.5, withdrawn), YoooP (5.0, rejected), SVFCL (4.33, withdrawn). Strong-band anchors scored 8.0+ (oral papers, clearly superior in novelty and rigor). **Initial bracket: 4.0–6.0.**

*Round 2 (narrowing):* Searched inside the bracket for adapter-based and prototype-based CIL papers. Retrieved OVOR (6.0, accepted poster — cleaner method, more datasets), MetaAdapter (5.4), SimpleCIL (4.75), YoooP (5.0), Dyn-Adapter (4.33), SVFCL (4.33), CREATE (4.8). Reading OVOR and MetaAdapter in full confirmed that the current paper is weaker than OVOR (6.0) which has clearer contributions, more datasets, and no factual errors. It is roughly comparable to MetaAdapter (5.4, rejected) — similar level of novelty and methodological concerns. The factual error in the parameter count claim (repeated in Abstract, Introduction, and Conclusion) is a concrete, verifiable weakness that MetaAdapter and OVOR do not have, pulling the paper downward relative to those anchors.

*Final placement:* The paper is weaker than OVOR (6.0, accepted) and roughly comparable to MetaAdapter (5.4, rejected) and SimpleCIL (4.75, withdrawn). The factual misrepresentation and limited evaluation scope (2 datasets, no variance) place it below the acceptance threshold for a competitive venue. **Score: 4.5.**

Anchors consulted across all rounds:
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| C-CLIP | 6.5 | 1 | More comprehensive; accepted poster — this paper is weaker |
| OVOR | 6.0 | 2 | Cleaner contribution; accepted poster — this paper is weaker |
| MetaAdapter | 5.4 | 1,2 | Similar novelty level; rejected — comparable quality |
| YoooP | 5.0 | 2 | Prototype method; rejected — comparable quality |
| SimpleCIL/APER | 4.75 | 1,2 | Simple approach with novelty concerns; withdrawn — slightly stronger due to more datasets |
| TIPS | 4.5 | 1 | Prompt-based CL; withdrawn — comparable |
| SVFCL | 4.33 | 2 | SVD fine-tuning for FSCIL; withdrawn — slightly weaker |
| CREATE | 4.8 | 2 | Auto-encoder prototypes; withdrawn — comparable |
| ProCEED | 3.0 | 1 | Exemplar-free with prototypes; withdrawn — weaker |
| LVLM-CL | 2.5 | 1 | VLM continual learning; withdrawn — weaker |

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>