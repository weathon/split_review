Now I have a comprehensive understanding of both the paper and the reviewer inputs. Let me construct the final consolidated review.

## Summary

The paper introduces Continuous Online Action Detection (COAD), a task formulation requiring models to both detect actions in real time and adapt parameters on-the-fly from streaming video under single-pass, no-replay constraints. The authors curate Ego-OAD, a large-scale egocentric OAD benchmark from Ego4D (87 classes, 263 hours, 22,991 instances). They propose three training strategies adapted to this setting — state continuity across windows, orthogonal gradient projection, and non-uniform loss weighting — and evaluate them on Ego-OAD and EPIC-KITCHENS, reporting gains in both in-stream adaptation and out-of-stream generalization over the pretrained-only baseline.

## Strengths

1. **Novel task formulation that fills a genuine gap.** COAD bridges offline OAD training and real-world deployment by requiring simultaneous online prediction and online learning under strict causal, single-pass constraints. This is a well-motivated problem that prior OAD work has not addressed. The paper clearly formalizes the setting (Section 4.5) and explains why it is particularly relevant for egocentric wearable devices.

2. **Large-scale egocentric OAD benchmark (Ego-OAD).** The dataset is curated from Ego4D Moment Queries and provides 87 fine-grained action classes, 22,991 labeled instances, and 263 hours of untrimmed egocentric video across diverse daily-life scenarios (Section 3). This fills a notable gap — prior OAD benchmarks are exocentric (THUMOS, TVSeries) or domain-limited (EPIC-KITCHENS). The dataset enables realistic evaluation of continuous learning in first-person settings.

3. **The method shows consistent generalization improvements on the main benchmark.** On Ego-OAD out-of-stream (Table 1, egocentric pretrain), COAD achieves 26.0 mAP / 76.0 Top-5 Recall vs. 25.5 / 71.6 for the naive adaptation baseline (w/o COAD). The ablation study (Table 3) confirms that each component contributes to out-of-stream generalization, and Figure 4 shows that COAD steadily closes the gap to an offline IID-trained upper bound as more in-stream data is processed, while ablated variants plateau.

4. **Thorough ablation analysis.** Table 3 systematically ablates each of the three proposed strategies (state continuity, orthogonal gradient, non-uniform loss), and Figure 3 explores the trade-off between in-stream and out-of-stream performance under different strides and learning rates. This provides insight into how the method balances adaptation and generalization.

## Weaknesses

### Major
- **The source of supervision during the continuous adaptation stream is not addressed.** The paper motivates COAD from the perspective of real-world wearable devices learning "on-the-fly," yet the experimental protocol assumes ground-truth multi-label annotations are available for every window (or at its final frame). While the paper notes that sparse labels suffice (a label every ~68 seconds at stride 128), it does not discuss how such supervision would be obtained in deployment (e.g., from user feedback, delayed annotations, or self-supervision). This gap between the motivating scenario and the evaluated setup weakens the practical framing. The authors should either explicitly scope the contribution as a method for settings where labels are periodically available, or discuss pathways toward weaker supervision.

### Minor
- **Headline improvement numbers are framed against the weakest baseline.** The abstract claims "up to 20% improvement in top-5 accuracy" — this compares COAD to the *Pretrained Only* model, which has seen no in-stream data. The marginal improvement over the more relevant *w/o COAD* baseline (which trains on the same data under the same single-pass constraint) is substantially smaller (e.g., +3.8 top-5 recall points on in-stream Exo, and on in-stream mAP COAD is sometimes *worse* than w/o COAD). The numbers are technically correct, but the framing inflates the perceived advantage of the proposed strategies over simple online training.

- **EPIC-KITCHENS results require deeper analysis and are only partially supportive.** Some patterns are anomalous: the pretrained-only model sometimes matches or exceeds both adaptation methods on in-stream metrics (e.g., Action mAP in-stream: Pretrained Only 9.6 vs. COAD 7.9), and the relative difficulty of in-stream vs. out-of-stream sets varies wildly across verb/noun/action categories. The paper's explanation ("fine-grained actions limit recurring pattern detection") is vague and does not address why the pretrained-only model — which has never seen the in-stream data — can outperform adapted models on it. This casts some doubt on the split design or the evaluation protocol for this dataset.

- **The data split design partly confounds data quantity with the continuous learning paradigm.** The in-stream set (1,177 videos, ~200h) is much larger than the pretraining set (186 videos, ~63h). Large gains from *Pretrained Only* to any adaptation method are expected simply from training on ~5× more data. The COAD vs. w/o COAD comparison partially controls for this, but a controlled experiment with equal total training data across conditions would more cleanly isolate the effect of the continuous-learning-specific strategies.

- **Individual technical components are adopted from prior work with limited modification.** State continuity during training, orthogonal gradient projection (Han et al., 2025), and non-uniform loss (An et al., 2023) are all existing techniques. The paper's novelty lies in the overall task formulation, the dataset, and the application of these techniques to OAD. The ablation shows these components are not always additive (full COAD has lower in-stream mAP than several ablations), and the paper does not introduce new algorithmic insight specifically tailored to the OAD structure.

- **No computational cost analysis is provided.** The paper claims suitability for resource-constrained wearable devices but provides no measurements of FLOPs, memory footprint, or latency for the online gradient update step (including the orthogonal projection overhead). This makes the claims about computational efficiency difficult to evaluate.

- **No explicit dataset release commitment.** For a benchmark contribution, a clear statement about dataset release and access mechanisms would strengthen the paper's impact on the community.

## Nice-to-Haves
- A variant where the same total amount of data is used for both the pretraining-only condition and the adaptation conditions, isolating the effect of the continuous paradigm from the effect of more data.
- Analysis of catastrophic forgetting with respect to the pretraining distribution (i.e., does adaptation on the in-stream degrade performance on classes seen only during pretraining?).
- Hyperparameter sensitivity analysis (learning rate, gradient projection strength).

## Removed Points
- **"Pretrained Only outperforms both adaptation methods on the out-of-stream set" (Harsh Critic, Issue 3):** This is not supported by the data. On EPIC-KITCHENS out-of-stream, COAD achieves the best or tied mAP on all three categories (Verb 11.8 vs. 11.4, Noun 37.1 vs. 31.4, Action 9.9 vs. 8.6). The critic's related numerical example ("Verb mAP: in-stream 11.4 vs out-of-stream 29.0") appears to misread the table's (out/in) ordering. 
- **"Technical novelty is too limited to be a contribution":** This criticism undervalues the paper's contributions in task formulation and dataset creation, which are separate from the method's component-level novelty. The paper does not claim to have invented these techniques; the contribution is the combination and application to a new setting.
- **"The IID upper bound in Figure 4 is not a realistic target for a storage-constrained system":** This is a misunderstanding — the IID baseline is explicitly framed as an unconstrained upper bound (standard offline training with multiple passes), not as a method that should be achievable under COAD constraints. The comparison is intended to show how close COAD gets to this oracle despite severe constraints.
- **"Table 4 (backbone comparison) is orthogonal to the paper's main claims":** While the backbones are compared under offline IID training rather than COAD training, this table informs a design choice (which backbone to use) and supports the claim that clip-level backbones benefit from egocentric pretraining.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful tension: the task formulation is genuinely novel and well-motivated, but the evaluation protocol does not fully bridge the gap to the motivating deployment scenario (specifically regarding label availability). This is a constructive observation that points toward a natural extension.

## Suggestions

1. Directly address the label supervision gap: either explicitly scope the setting as "online adaptation with periodically available labels" and discuss realistic sources (user corrections, offline annotation cycles), or demonstrate a pathway to weaker supervision (e.g., self-supervised objectives on unlabeled portions of the stream).
2. Reframe headline claims to transparently show the marginal benefit over the naive single-pass baseline (w/o COAD) alongside the absolute gain over the pretrained-only lower bound.
3. Provide a more thorough analysis of the EPIC-KITCHENS split and results, explaining the anomalous patterns (e.g., why the pretrained-only model sometimes exceeds adapted models on in-stream data).
4. Include computational cost measurements (FLOPs, memory, latency per update step) to substantiate the suitability claim for resource-constrained devices.
5. Add a controlled experiment equalizing total training data across conditions to isolate the effect of the continuous paradigm from the effect of data quantity.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>