## Summary
CaPT proposes an asymmetric co-training framework that integrates CLIP into semi-supervised learning (SSL) to break the "label dependency" bottleneck. A unimodal network (fully fine-tuned) and a CLIP model (adapter-tuned via PEFT) are jointly trained using entropy-weighted co-pseudo labels. The authors theoretically motivate the approach via a Gaussian-mixture prototype model showing pseudo-label error worsens with sparse or low-quality labels, then empirically demonstrate that CaPT achieves state-of-the-art SSL performance, with especially large gains in extreme low-label regimes (e.g., +21.38% on CIFAR-100, 1-shot).

---

## Strengths

- **Compelling theoretical motivation and supporting empirics**: Theorem 1.1 formalises the claim that pseudo-label error grows exponentially as the labeled-set quality/quantity shrinks, and Figure 1b,c directly validates this on real training runs of FreeMatch. The theory grounds the paper's central observation in a principled way rather than relying on empirical observation alone.

- **Large, reproducible performance gains in extreme low-label regimes**: On CIFAR-100 (1-label/class), CaPT achieves 82.51% vs. 60.49% (RegMixMatch, 2nd best), a 21.38% absolute improvement. On ImageNet (10-labels/class), CaPT improves over RegMixMatch by 9.33 Top-1 points. These are not marginal margins; they represent a qualitative shift in capability at the practically relevant very-low-supervision operating point.

- **Practical efficiency**: Table 4 shows CaPT adds only 8% memory and 11% training time over FreeMatch, which is much cheaper than RegMixMatch (+40% memory, +58% time) while delivering far better accuracy. This makes the method genuinely deployable rather than a research artifact.

- **Thorough ablation study**: Table 6 systematically tests each design choice (co-training direction, adapter vs. full-finetune, feature augmentation, entropy vs. equal weighting). Each ablation has a clear motivation, and the numbers support the design rationale without exception.

- **Attention to evaluation validity**: By testing on 6 fine-grained benchmarks (Flowers102, StanfordCars, SUN397, DTD, SVHN, FGVCAircraft) that diverge from typical CLIP pretraining data, the authors pre-empt the obvious concern that CLIP's data overlap with simple benchmarks explains the gains. CaPT remains competitive or best on 5 of 6 of these.

---

## Weaknesses

### Fatal
None.

### Major

- **Inconsistent reporting of CaPT's final output on STL-10**: The paper states it reports the **unimodal network (UPM)** as CaPT's final result. On STL-10 (4 labels/class), this gives 96.07%, while the adapter-tuned CLIP (MPM) component within the same CaPT run achieves 96.86%, and CLIP zero-shot is 97.18%. The co-training framework's unimodal output is therefore *worse* than simply adapter-tuning CLIP alone on this dataset. The paper does not explain this anomaly or discuss when co-training benefits vs. hurts the unimodal branch. If STL-10 is a near-saturation case for CLIP (97.18% zero-shot), the paper should acknowledge this explicitly and clarify why the unimodal network is always the designated output rather than, e.g., the ensemble or the better-performing branch.

- **FGVCAircraft underperformance left unaddressed in the main paper**: On FGVCAircraft (5 labels/class), CaPT (50.12%) underperforms FreeMatch (51.43%). The paper defers entirely to Appendix N without even a brief sentence in the main body explaining the failure mode. For a method whose main contribution is the reliability of CLIP's prior, a case where CLIP-guided co-training harms performance deserves at least a brief inline explanation.

### Minor

- **Theorem 1.1 rests on a Gaussian-mixture prototype model** that is a significant simplification of deep-network feature dynamics (non-linear representations, learned prototypes, normalization layers, etc.). The theorem is a useful intuition pump, but the paper does not discuss whether the bound remains informative for the actual architectures used (ViT-B). A brief remark on the gap between the model and practice would strengthen the theoretical section.

- **Attention map analysis in Figure 3 is qualitative and cherry-picked**: The claim about cross-modal complementarity is compelling conceptually, but the evidence is 8 cherry-picked examples. A quantitative measure (e.g., CKA similarity between UPM and MPM representations over the whole evaluation set) would substantially strengthen this point.

### Trivial

- The use of $\arg\max$ in Equation (3) returns a hard label, but it is then combined in Equation (13) in a soft convex combination. The distinction between hard and soft pseudo labels in PFM is not made fully explicit and could cause reader confusion.

---

## Nice-to-Haves

- Report ensemble accuracy (average UPM and MPM predictions at inference) alongside the unimodal-only result to give practitioners the best possible number and to contextualize the STL-10 anomaly.
- Include a direct ablation where adapter-tuned CLIP is trained *without* co-training against UPM (i.e., adapter-tuned CLIP + SSL data, standalone), as a cleaner baseline to isolate the co-training gain from the CLIP prior gain.
- A cross-dataset summary figure showing where CaPT helps most vs. least (as a function of CLIP zero-shot accuracy) would crystallize the practical guidance for when to apply the framework.

---

## Novel Insights

CaPT surfaces a previously underemphasised failure mode of SSL: the utility of unlabeled data is not independent of labeled data quality, but is exponentially sensitive to it. By introducing an asymmetric-modalities co-training setup—where CLIP provides reliable priors even when the labeled set is near-empty—the paper shows that a frozen vision-language model can serve as an "external scaffold" that unlocks unlabeled data exploitation independent of labeled-set quality. The entropy-weighted label fusion, which transitions supervision weight from CLIP to the fully fine-tuned network as training progresses, is a clean operationalisation of this scaffold role. This dynamic handoff mechanism, together with feature-level Mixup inside a frozen encoder to avoid redundant high-resolution forward passes, represents a practical template for efficiently pairing any VLM with any SSL algorithm.

---

## Suggestions

- Directly address the STL-10 result in the main paper: hypothesize or empirically confirm that when CLIP zero-shot accuracy is ≥ ~96%, CaPT's co-training transfers less to the unimodal branch, and suggest practitioners use the MPM output directly in such cases.
- Add a standalone "adapter-tuned CLIP without co-training" row to Table 1 and Table 3 so readers can isolate the co-training contribution from the CLIP prior contribution.
- Clarify the pseudo-label representation in PFM: state explicitly whether $\hat{q}^a$ and $\hat{q}^b$ are one-hot vectors or soft distributions, since this affects how the convex combination in Eq. (13–14) is interpreted.

---

## Score and Decision

CaPT addresses a real and practically important failure mode of SSL (label dependency in extreme low-supervision regimes), provides both theoretical and extensive empirical support, and offers a portable, efficient framework. The primary weakness—unexplained CaPT underperformance relative to its own CLIP component on STL-10—is notable but does not undermine the core contribution, as STL-10 is a near-saturation dataset for CLIP. The paper's strong results on CIFAR-100, ImageNet, EuroSAT, and the fine-grained benchmarks make a compelling case. The method is clearly presented with thorough ablations and honest efficiency reporting.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>