Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes COGT (Causally-Ordered Generative Training), a method that uses an off-the-shelf dependency parser to define a Causal Graphical Model over the words in a caption. The resulting dependency structure is used to define a partially-ordered, semi-parallel autoregressive training objective that conditions each word only on its ancestors in the dependency tree and on visual features. Applied as a fine-tuning decoder on top of frozen VLMs (CLIP, XVLM, InstructBLIP), COGT achieves large and consistent improvements across five compositional benchmarks, often by double-digit percentage points over prior methods including those trained on orders of magnitude more data.

## Strengths

- **Strong and consistent empirical results across diverse backbones and benchmarks.** Table 3 shows COGT-CLIP (trained on only ~100K COCO captions) achieves an average accuracy of 79.25 across five compositional benchmarks, outperforming the next best CLIP-based method (DAC-LLM, trained on ~3.3M CC3M samples) by 12.27 absolute points. Tables 4 and 5 confirm this pattern holds for XVLM and InstructBLIP backbones, establishing a new state of the art.

- **The core idea — using syntactic dependency parse to define a partially-ordered generative process — is clean, novel, and well-motivated.** Table 1 directly validates this: COGT outperforms Sequential-AR (+3.1 avg), Fully-Parallel (+17.77), and Mixed/CapPa-style (+5.7) strategies under controlled conditions (same backbone, same data, same decoder size). This shows the dependency structure, not just generative training, drives the improvement.

- **Ablations systematically validate the key design choices.** Table 2 demonstrates the contribution of each component: replacing mask-specific tokens with a generic BERT mask drops accuracy by 2.69 points; using only the last CLIP layer instead of two layers drops accuracy by 4.75 points; parser quality directly correlates with downstream performance (Deep Biaffine+RoBERTa > CRFPar > Deep Biaffine). These controlled experiments give confidence that the reported gains are attributable to the claimed mechanisms.

- **Method generalizes across multiple VLM families and training scales without degrading standard capabilities.** COGT is successfully applied to CLIP, XVLM, and InstructBLIP, scaling from COCO alone to COCO+CC3M+Visual Genome. Table 6 shows COGT does not hurt (and can slightly improve) standard image classification features under linear probing, addressing a known concern in compositional fine-tuning.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The causal framing is stronger than what the paper validates, and the core contribution does not depend on it.** The paper argues that dependency parser relations are "causal" in a Pearlian sense (interventions, counterfactuals), but what the method actually implements is a dependency-guided generation order that avoids spurious associations induced by linear word order. The paper partially acknowledges this (Sec. 3 Discussion: "While the causal dependency relations in C may not be exhaustively described by G… we prefer sparseness to completeness"), but the title, method name (Causally-Ordered Generative Training), and motivating framing in the abstract and introduction consistently invoke the full CGM machinery (causal sufficiency, disentangled factorization). The empirical gains are real regardless of whether one accepts the causal interpretation — they could equally be attributed to a better inductive bias from the syntactic tree structure. Reframing as "syntactically-guided generative training" would be more accurate and would not require assumptions that are not validated. This does not affect the paper's empirical contribution but overstates the theoretical grounding.

2. **The ablation study does not include a control for random dependency structure.** Comparing COGT to Sequential-AR and Fully-Parallel (Table 1) shows that a dependency-guided order is better than left-to-right or fully independent orders. However, this confounds two factors: (i) the specific parent sets from the dependency parser, and (ii) the fact that the attention is structured and non-sequential. Adding a baseline with **random** dependency graphs (same DAG topology but random parent assignments per caption) would settle whether the parser's specific structure is responsible or simply any non-sequential ordering. Table 2 shows that better parsers yield better results (indirectly supporting the parser's value), but a random-structure control would be cleaner evidence for the claim that "the dependency parser provides a priori knowledge."

3. **The comparison to Cap/CapPa (Table 5) is informative but not apples-to-apples.** COGT-XVLM+ and COGT-InstructBLIP+ outperform Cap and CapPa despite training on far less data. However, Cap and CapPa are pre-trained from scratch on 1B image-text pairs, while COGT adapts already-pretrained VLMs with an additional decoder. The gap could partly reflect base VLM quality rather than the COGT method. The paper acknowledges this difficulty ("a direct comparison… is difficult"), but the claim of "new state of the art" in Table 5 would benefit from explicitly positioning COGT as a **fine-tuning method** that improves compositional understanding of any VLM, rather than as a direct competitor to full pre-training. A cleaner comparison would apply COGT on top of Cap/CapPa's backbone to show additive gains.

4. **Training and evaluation benchmarks substantially overlap in image source (COCO).** ARO, SugarCrepe, VL-CheckList, and ColorSwap are all built from COCO images — the same source used for COGT training. This follows the field's standard protocol (Yuksekgonul et al., 2023; Zhang et al., 2024), so cross-method comparisons are fair. However, the paper's claim that COGT "generalizes" would be strengthened by a held-out evaluation on a non-COCO compositional benchmark. The paper mentions Winoground results in the appendix (stripped by parser), which partially addresses this. Without explicit reporting of out-of-distribution performance, the generalization claim is somewhat weaker than presented.

### Trivial
None.

## Nice-to-Haves

- An analysis of failure cases showing what types of compositional errors COGT still makes (e.g., rare syntactic structures, cases where the dependency parser itself is incorrect).
- A brief discussion of the computational overhead of running a dependency parser at inference time for each candidate caption.
- An analysis of whether COGT is robust to moderate parser noise (e.g., by injecting random noise into training dependencies).

## Removed Points

- **Criticism that the causal interpretation discussion is "only in passing (Sec. 2)."** The discussion is a full paragraph in Sec. 3 (lines 69–77) that explicitly addresses the causal interpretation and its limitations. The underlying concern (overblown framing) is kept as a minor weakness, but the "in passing" characterization is inaccurate.
- **Criticism about missing appendix details (FG-OVD construction, Winoground results).** The parser strips appendix sections from all papers; these exist in the original submission per the authors' statement. The broader concern about COCO-domain overlap is retained in minor weaknesses.
- **Strength #5 from Strength Finder ("Principled use of syntactic parsing as causal prior, supported by linguistic leaderboard metrics").** This conflicts with the verified weakness that the causal framing is overblown and not rigorously validated. Per the rule that weaknesses win over conflicting strengths, this strength is removed.

## Novel Insights

Beyond the paper's own contributions, the pattern of results offers an interesting insight: **the benefit of syntactic guidance is not marginal — it is very large.** The +17.77 point gap over Fully-Parallel and +3.1 over Sequential-AR (Table 1) suggests that the choice of factorization for the generation process matters far more than the field may have expected. The finding that a frozen visual encoder + small decoder with dependency-guided attention can beat end-to-end methods trained on 10× more data (Table 3) indicates that the primary bottleneck in compositional VL understanding may not be visual representation quality but rather how text is modeled relative to vision. This is a provocative suggestion worth further investigation.

## Suggestions

1. Soften the causal framing throughout the paper: reframe the contribution as "using syntactic dependency trees to define a partially-ordered generative process that reduces spurious dependencies induced by linear word order." This drops unnecessary assumptions without weakening the empirical claims.
2. Add a random-dependency ablation to Table 2 to confirm that the parser's specific structure, not just any non-sequential order, drives the gains.
3. In Table 5, explicitly qualify the comparison to Cap/CapPa (e.g., note that COGT is a fine-tuning method on strong base VLMs, not a from-scratch pre-training approach) to avoid the appearance of an unfair comparison asymmetry.
4. Report held-out (non-COCO) evaluation numbers more prominently — move Winoground results from the appendix into the main paper, or add a brief discussion of out-of-distribution performance.

## Score and Decision

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>