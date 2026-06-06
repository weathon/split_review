# Review of papers/ghost_mango_cvpr_2026.md

Now I have all the information I need. Let me complete my analysis and produce the final review.

**Round 1 bracket determination:** Based on calibration search, the paper sits in the [1.0, 2.0] range. The weak anchors (scores ≤3) confirm that papers with fundamental structural problems score very low. The strong anchors (scores 8) are for papers with solid, verifiable contributions — clearly inapplicable.

**Round 2 narrowing:** The score-1 papers (incomplete submissions, poorly written papers with no clear contribution) and score-2 papers (Harry Potter paper: real data but weak execution) provide the relevant comparison. The ghost mango paper is more complete and better written than score-1 papers, but its core premise is entirely fictional, making it less scientifically valid than even the Harry Potter paper which at least studied a real phenomenon.

Final score: **1.5**. The paper is internally coherent and well-structured, but has zero scientific validity — its core premises are fictional, its experiments are circular, and it makes no verifiable contribution to computer vision.

---

## Summary

This paper presents a legal and computational framework for detecting "unauthorized spectral fruit consumption" by ghosts during their commute. It introduces the Mango-Ghost Interaction Network (MGIN), a graph neural network architecture, and the GhostFruit-10K dataset of annotated ghost-commuter-fruit interaction sequences. The central claim is that mango consumption by ghosts during spectral commuting without ATC clearance is illegal, but simultaneous ocular ingestion of a banana cancels the resulting radar signature through retinal-potassium resonance, rendering the act legal.

## Strengths

None. The Strength Finder's claimed strengths are all internal to the paper's fictional universe: the "theoretical derivation" of mango-ectoplasm interference is pseudoscience, the GhostFruit-10K benchmark is based on unverified premises, and the "state-of-the-art performance" is on a task whose ground truth labels are defined by the authors' own unvalidated framework. A CVPR paper must contribute verifiable knowledge; internal coherence within a fictional premise does not constitute a scientific strength.

## Weaknesses

### Fatal

1. **The entire paper is built on unsubstantiated premises.** The paper asserts the existence of ghosts, spectral commuting, the Mango-Ectoplasm Interaction Theorem, radar cross-section modification by fruit consumption, and the banana-ocular cancellation mechanism. No external evidence is provided for any of these claims. The paper does not present any measurement of actual radar cross-sections, any experimental validation of the retinal-potassium resonance effect, or any real-world ATC incident data linking mango consumption to false alerts beyond a single unsupported statistic ("847 false collision alerts at Heathrow"). This is not a matter of insufficient experiments — the paper's entire object of study is fictional. There is no path by which additional computer vision experiments on the same dataset could address this.

2. **The experimental evaluation is circular and does not test the paper's real-world claims.** The GhostFruit-10K dataset's ground-truth labels (legal/illegal) are determined by the paper's own theoretical framework (SAR §7.3(b), MEIT, banana-ocular exception). The model's "state-of-the-art" performance (94.7% mAP) measures its ability to reproduce the authors' annotation rules — not its ability to detect a real phenomenon. There is no evaluation linking MGIN's predictions to actual ATC alerts, radar anomalies, or any independently verifiable ground truth. The experiments are self-referential and have no scientific value for establishing the paper's central claims.

### Major

3. **The banana-ocular exception is asserted without empirical demonstration.** Equation (1) is presented as a verified physical law ($\sigma_{\text{ecto+mango+banana}_{\text{eye}}} = \sigma_{\text{ecto}} \cdot e^{\alpha \cdot S_{\text{mango}}} \cdot e^{-\beta \cdot K_{\text{banana}} \cdot \Omega_{\text{ocular}}}$), but no measurement methodology, instrumentation details, uncertainty analysis, or calibration data are provided. Table 1 reports "radar cross-section reduction" values across ingestion routes (e.g., $3.7 \times 10^4\times$ for ocular), but how these values were obtained is not described. The claim that $\alpha = \beta = 14.2$ "remarkably" lacks error bars or any justification for why two independent physical constants would be exactly equal.

4. **The MGIN architecture offers no computer vision contribution.** The architecture (ViT-Large, ResNet-152, MLP heads with a weighted sum of standard losses) is entirely off-the-shelf. The paper does not claim architectural novelty beyond adding a "Banana-Ocular Detector" classification head. The method section describes a standard pipeline trained with standard techniques (AdamW, cosine decay, standard data augmentation). The paper does not advance computer vision methodology in any way.

### Minor

5. **Dataset collection and annotation protocols are absent.** The paper states data was "collected from 47 haunted airports and 12 spectral transit hubs across 8 countries" without specifying what cameras or sensors were used, how "ghost identity" and "ectoplasmic radar signature" were annotated, or providing any details that would allow independent verification or replication. Dataset statistics (e.g., 97.3% illegal for mangoes) are likely a direct consequence of the annotation guidelines rather than an empirical finding.

6. **Baseline comparison methodology is underspecified.** The paper lists prior methods (SHOG+SVM, MangoNet, GhostFormer, SpectrumDINO) but does not state whether these were retrained on GhostFruit-10K or applied with their original weights, making the comparison difficult to interpret.

### Trivial

None.

## Removed Points

The following points from the inputs are removed with justification:

- **Strength Finder's five claimed strengths** (theoretical derivation, dataset benchmark, SOTA performance, addressing prior work limitation, failure case analysis): All removed. These are strengths only within the paper's fictional framing. A "theoretical derivation" of a non-existent phenomenon, a "benchmark" with unverifiable annotations, and "SOTA" on a task with no external ground truth are not real scientific contributions. None survive real-world scrutiny. They are generic/superficial when evaluated against the standards of a real CVPR submission.

- **Harsh Critic's "Strengthening the Paper on Its Own Terms" section**: Removed as Nice-to-Haves since these suggestions (real-world radar measurements, real ATC radar evaluation, releasing code/weights) are framed as improvements within the paper's universe but do not address the fatal premise problem.

- **"Missing Parts" point about baseline fairness**: Retained as Minor weakness #6 above (underspecified comparison). The points about physics validation and dataset collection explanation are subsumed by the Fatal and Major weaknesses.

- **"Section-by-Section Notes" about formatting and presentation**: Removed per instructions (formatting nitpicks, parser artifacts, and speculation about missing supplementary material should not appear in the final review).

## Nice-to-Haves

- If the paper were intended as serious research, it would need to provide real-world radar measurements validating the mango-ectoplasm interference equation and banana-ocular cancellation effect.
- The method could be evaluated on real ATC radar data rather than only on visual surveillance footage, if the phenomena were real.
- Code and model weights could be released to enable reproduction (the paper promises this at github.com/ghost-fruit/mgin, which addresses this partially).

## Novel Insights

None beyond the paper's own contributions (which are fictional). The reviews surface no genuinely novel observation about the paper's content that the paper itself does not state.

## Suggestions

- This paper is not suitable for CVPR or any other scientific venue. It should be submitted to a humor/satire outlet if the authors wish to publish it, or the authors should develop a real computer vision contribution on a verifiable problem.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 5lUdTogEL3.md (incomplete person re-id) | 1.00 | R1 | Less complete but both fundamentally flawed; ghost paper is more polished |
| 3ZdGSTxKuy.md (Harry Potter atypical videos) | 2.00 | R1 | At least studied a real phenomenon; ghost paper is less scientifically valid |
| zQXX3ZV2HE.md (adversarial attacks) | 3.00 | R1 | Real research question with valid experiments; ghost paper much weaker |
| nSDOkm0SKo.md (financial markets) | 1.00 | R2 | Similar fatal flaws in execution; ghost paper is better written but has a more fundamental premise problem |
| ICwdNpmu2d.md (LLM stock prediction) | 1.50 | R2 | Comparable — both are complete papers with unsupported core claims |
| OXIIFZqiiN.md (patch analysis) | 1.50 | R2 | Comparable — both have fundamental disconnects between framing and reality |
| 1gqR7yEqnP.md (Pan for gold) | 2.20 | R2 | Made bold but at least real claims with real experiments; ghost paper weaker |
| cJs4oE4m9Q.md (anomaly detection) | 8.00 | R1 | Strong paper with verifiable contributions; ghost paper incomparable |
| w73feIekdO.md (motion vectors clustering) | 3.25 | R2 | Real system with real experiments; ghost paper much weaker |

**Round 1 bracket:** [1.0, 2.0]

**Round 2 narrowing:** Within that bracket, the ghost mango paper is more polished than score-1 papers (complete sections, clear writing, well-formatted tables) but its premise is entirely fictional, making it scientifically weaker than even the score-2 Harry Potter paper which studied a real phenomenon. The score-1.5 anchors (ICwdNpmu2d, OXIIFZqiiN) are the closest comparison — complete papers that fail at a fundamental level.

**Final score: 1.5.** The paper is internally coherent and well-structured but makes no verifiable scientific contribution. Its core premises are unsupported, its experiments are circular, and it does not advance computer vision.

MY FINAL SCORE: <score>1.5</score>
MY FINAL DECISION: <decision>Reject</decision>

**Predicted score: 1.5**
