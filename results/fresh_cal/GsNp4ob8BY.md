Now I have a complete picture of the paper. Let me synthesize the review.

## Summary

This paper introduces "ability tokens" — learned embeddings added to a frozen LLM's embedding matrix — that function like a markup language for specialized domains. Two token types are proposed: domain markers (encoding domain-level knowledge, e.g., for SMILES strings) and functional tokens (encoding task instructions, e.g., predict QED score). A three-stage hierarchical training protocol learns these tokens progressively from unlabeled to supervised data. The method is evaluated on multilingual translation and biomedical tasks (molecular property prediction, drug combination, binding affinity) using LLaMA-7B, achieving state-of-the-art on TDC Drug Combination and competitive performance on Binding Affinity.

## Strengths

- **State-of-the-art on a real benchmark**: The method achieves SOTA on the TDC Drug Combination (DrugComb CSS) benchmark, outperforming both LM-based baselines (LoRA, prompt tuning) and the domain-specific expert model DeepDDS (Xia et al., 2018). This provides concrete evidence for the claim that the markup system can match specialized task-specific models. (Section 4.2.2, Table 3)

- **Ablation study validates component design**: Figure 3 (right) systematically ablates each component — removing the regression head causes the largest performance drop, removing the functional token or domain marker also degrades results, and marker enrichment (QED-pretrained marker vs. non-enriched) provides a clear improvement. This gives controlled evidence that all three design elements contribute. (Section 4.2.2, lines 175-179, Figure 3)

- **Parameter efficiency vs. strong baselines**: The method uses 40,960 parameters per ability token (just 0.0005% of LLaMA-7B's parameters). Table 2 shows it outperforms LoRA (which uses substantially more parameters) on both protein descriptor prediction (MSE 0.033 vs. 0.046) and QED prediction (MSE 0.182 vs. 0.214), demonstrating a favorable parameter-performance trade-off. (Section 4.2.1, Table 2)

- **Cross-domain modeling validation**: The Binding Affinity experiment (Section 4.2.3) requires combining protein and SMILES domain markers with a functional token, testing the framework's ability to handle multi-instance, cross-domain inputs. The method outperforms all LM-based baselines under distribution shift (split by patent year), providing evidence that the token framework generalizes beyond single-domain settings.

## Weaknesses

### Major

- **The method's claimed advantage of preserving general language capabilities is asserted but never tested**. The paper repeatedly frames this as a key differentiator from fine-tuning (abstract: "preserving the pretrained weights and the model's original capabilities"; line 12: fine-tuning methods "compromise the model's general abilities"; line 14: "the pretrained weights remain intact and the model's general language capabilities are retained"). However, no experiment evaluates performance on any general-purpose benchmark (e.g., MMLU, HellaSwag, standard NLU tasks) before and after adding ability tokens. Because the learned embeddings are added to the embedding matrix, they could theoretically interfere with the model's behavior on unrelated inputs. This is a structural gap — the paper makes a central promise that it does not verify. (Abstract, lines 12–14, lines 196–201)

- **The compositionality claim — a headline contribution — is not supported by visible results in the main text**. Section 4.1 (the modular multilingual translation experiment) only describes the setup (8 language markers, 5 paired training language pairs) but presents zero quantitative results — no BLEU scores, no tables, no comparison of unseen pairs vs. baselines. The paper repeatedly highlights compositionality as a key advantage over prior work (abstract, line 30, line 97), and the introduction of the section states the goal is to "verify (i) if the markers can correctly extract the domain information from the data (modularity); and (ii) the learned functional token can generalize to unseen domains and translation pairs (compositionality)" — but the results are neither in the main text nor verifiable from this extraction. For such a differentiating claim, this is a significant presentation gap. (Section 4.1, lines 132–141; also abstract, line 30)

- **No statistical rigor in experimental reporting**. The paper reports point estimates only — no standard deviations, confidence intervals, or number of experimental runs for any of the main results (Tables 2, 3). Dataset sizes are not specified. Train/val/test splits are not described for the molecular property prediction tasks. Given that the paper makes comparative claims ("significantly outperforms", "outperforming all LM-based baselines"), the absence of variance information makes it impossible to judge whether the reported advantages are statistically reliable. (Sections 4.2.1–4.2.3, Tables 2 and 3)

- **Parameter-count comparison with prompt tuning is imprecisely stated**. The paper claims (line 161) that prompt tuning has "the same number of learnable parameters as our method." However, the method includes a regression head (4096 × output_dim parameters) in addition to the functional token (40,960 parameters), bringing the total above the 40,960 parameters of a 10-token prompt-tuning prefix. Without clarifying whether the baseline also uses a regression head, or specifying the exact parameter counts, the claim of parameter-equivalent comparison is misleading. (Line 128, line 161)

### Minor

- **The SOTA claim on Drug Combination is against a single 2018 expert model**. The paper states (line 170) that it "outperform[s] not only all LM-based baselines but also the domain-specific expert model (Xia et al., 2018)." While the result is valid, the TDC leaderboard likely includes more recent deep learning methods; comparing against a single 2018 model weakens the "state-of-the-art" claim. The paper does not report the complete leaderboard standings.

- **Missing experimental details for the three-stage protocol**: (a) The quantity and source of unlabeled data used for domain marker training is not specified (line 155 merely says "unlabeled data extracted from Blanchard et al. (2021)" without numbers). (b) The loss combination during Stage 2 (marker enrichment) is not specified — the paper says markers are updated with "ℓ_M" (next-token prediction loss) and "ℓ_F" (task loss) but does not state whether these are weighted equally or how the weighting was chosen (lines 106, 117). (c) It is unclear whether the baselines (prompt tuning, LoRA) also use regression heads for the numerical prediction tasks, which would affect whether observed gains come from the tokens or the output head.

- **Ablation does not control for parameter count**. When the domain marker or functional token is removed in the leave-one-out analysis (Figure 3, right), the parameter count also changes. While the ablation is informative, the paper's conclusion that "all three components are crucial" would be strengthened by a comparison against a prompt-tuning baseline with the same total parameter budget as the full method. (Figure 3, lines 177–179)

- **The method is evaluated on only one base model (LLaMA-7B)**. Results on at least one additional model (e.g., a smaller LLaMA variant or a different architecture) would increase confidence that the findings generalize rather than being specific to this model.

### Trivial

None.

## Nice-to-Haves

- Include dataset sizes (number of training examples) for all experiments.
- Compare against more recent methods on the TDC Drug Combination leaderboard beyond the 2018 baseline.
- Add a probing or embedding-similarity analysis to verify that domain markers actually encode domain-level semantics.
- Explore classification and structured prediction tasks beyond regression.

## Removed Points

Some criticisms from the reviewers are removed with justification:

- **Harsh Critic's claim that compositionality results are "deferred to Appendix B.1" is removed as a weakness about missing appendix content** — the hard rule states to remove criticisms about missing appendix sections, as these are stripped by the parser. However, the related point that the main text itself contains *no* results for Section 4.1 is retained as a major weakness (see above), because it is a verifiable gap in the main text's presentation.

- **Harsh Critic's criticism that the nearest-neighbor baseline is "weak"** is removed — it is just one of several baselines (including LoRA, prompt tuning, linear probing, hard prompting). Including a simple baseline does not weaken the method's results against stronger ones.

- **Strength Finder's claim that Section 4.1 "reports" compositionality results** is removed as unsupported — the visible text of Section 4.1 contains no results, only setup description.

- **Harsh Critic's complaint about missing effect sizes from garbled tables** is partially removed — the garbled table formatting is a parser artifact. However, the absence of standard deviations, confidence intervals, and dataset sizes in the *textual* discussion is a genuine weakness retained above.

- **Harsh Critic's complaint about "no evaluation of ability token training efficiency"** is removed as excessive scope creep — the paper's scope is effectiveness, not data-efficiency quantification.

- **Harsh Critic's complaint about "missing discussion of potential negative effects"** is removed as speculative.

- **Strength Finder's generic strength about "marker enrichment improves performance"** is merged into the ablation strength.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same issues (compositionality evidence, missing general-capabilities check, statistical rigor) and the same strengths (SOTA on Drug Combination, clean ablation). The main novel observation from synthesis is that the paper's most differentiating claim (compositionality) and its most frequently repeated advantage (preserving general capabilities) are the two least-supported parts of the submission — a pattern that suggests the paper overclaims relative to what it actually demonstrates.

## Suggestions

1. **Add a brief general-capabilities sanity check**: Evaluate LLaMA-7B on 3–5 standard NLU benchmarks (e.g., MMLU subsets, HellaSwag) before and after adding ability tokens. Even a single table with 4–6 tasks would substantiate the preservation claim.

2. **Move compositionality results into the main text**: Present a concise table in Section 4.1 showing BLEU scores for seen and unseen translation pairs, demonstrating that a single ⟨Translate⟩ functional token combined with different language markers works zero-shot. This is the paper's most differentiating feature and must not be deferred.

3. **Add error bars or at minimum report the number of runs** for all main results (Tables 2 and 3). State dataset sizes and train/val/test splits explicitly.

4. **Clarify the parameter-count comparison**: State how many parameters the prompt-tuning baseline uses (including whether it has a regression head), and exactly how many the full method uses (functional token + regression head). If the comparison is not perfectly matched, acknowledge the difference and discuss its potential impact.

5. **Qualify the SOTA claim** by noting which version of the TDC leaderboard is used and whether more recent submissions exist, or add comparisons against additional methods.

## Score and Decision

**MY FINAL SCORE: <score>5.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**