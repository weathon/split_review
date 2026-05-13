Now I have a thorough understanding of the paper. Let me carefully verify the key criticisms against the actual paper content before composing the final review.

## Summary

The paper proposes two methods for using pre-trained frozen language models to guide visual representation learning: Explicit Language Guidance (ExLG), which aligns visual features to text-derived embeddings via a similarity-preserving loss, and Implicit Language Guidance (ImLG), which inserts a frozen language model transformer block into the vision pipeline to process visual features. Both are evaluated across five domains: IID/OOD generalization, shortcut learning, texture bias, adversarial robustness, and continual learning, showing improvements over vanilla baselines.

## Strengths

- **Broad empirical evaluation across multiple generalization and robustness axes**: The paper evaluates on IID accuracy, OOD benchmarks (ImageNet-A/R/O), shortcut learning (Skewed-CelebA, Tinted-CIFAR10), texture bias (stylized TinyImageNet), adversarial robustness (PGD attacks), and continual learning (Seq-CIFAR10, Seq-TinyImageNet). This breadth allows the reader to assess where language guidance helps and where it doesn't (Section 5, Tables 1–3, Figures 4–7).

- **Strong and meaningful shortcut-learning improvements**: On Skewed-CelebA, ImLG improves overall accuracy from 61.28 to 75.90, with striking gains on minority subgroups (94% relative improvement for non-blonde females). These are not marginal gains on a toy problem—they address a well-known, practically important failure mode of neural networks (Table 2, Section 5.2).

- **Differentiated behavior between ExLG and ImLG**: The finding that ExLG excels in IID settings while ImLG shows stronger OOD robustness and adversarial resilience at high perturbation strengths (Figure 5) adds genuine nuance to the results. This suggests the two forms of guidance operate through different mechanisms rather than just "adding language helps everything" (Section 5.1, 5.4).

## Weaknesses

### Fatal
None.

### Major

- **No ablation controlling for the origin of ImLG's frozen weights**: This is the single most important gap. ImLG inserts a frozen transformer block from a language model into the vision pipeline, where it processes visual (not textual) features. The paper claims this provides "implicit language guidance" and "acts as a conceptual filter" drawing on "higher-level abstractions derived from language" (Sections 4.2, 5.2, 5.4). However, the most essential control experiment—replacing this frozen LM block with a randomly initialized transformer block of the same architecture—is entirely absent. Without it, one cannot conclude that the observed improvements come from *language-derived* inductive biases rather than from simply adding an attention module with a particular structure. Table 4 compares different language models but still omits the random-initialization baseline, making it impossible to determine whether LLAMA outperforms Sentence Transformer due to language knowledge or due to model capacity. This gap directly undermines the paper's central claim that *language* guidance is the active ingredient in ImLG.

- **Limited baseline comparisons and no parameter-matched controls**: Across all evaluations, the paper compares against vanilla ResNet-18 (or Experience Replay for continual learning). For shortcut learning, established methods like Group DRO go unmentioned; for adversarial robustness, adversarial training is absent; for continual learning, only ER is compared despite stronger methods like DER++ being standard. Additionally, ImLG adds an entire frozen transformer block plus mapping layers to the vision pipeline, introducing both parameter count and architectural capacity that the baseline lacks. Without a parameter-matched control (e.g., a wider ResNet or a ResNet with an added convolutional block), the improvements from ImLG could be attributed to increased model capacity rather than language-derived inductive bias. This concern compounds the previous ablation gap.

### Minor

- **The ImLG narrative overclaims "language guidance"**: At inference time, no text whatsoever passes through the frozen LM block—it receives projected visual features and outputs transformed visual features. Calling this "language guidance" and claiming it transfers "abstract, high-level concepts from language" (Section 4.2) is a strong narrative commitment that the evidence does not support, given the missing ablation. The paper would be more honest in framing ImLG as "language-initialized guidance" or "frozen-language-model-weight guidance" and explicitly acknowledging that verifying whether the language origin matters is an open question. This is not merely cosmetic—misframing obscures the actual scientific contribution (which may be about architectural inductive biases rather than linguistic ones).

- **No examples or analysis of class descriptions in ExLG**: The paper states descriptions are "generated either manually or using models like GPT" (Section 4.1) but provides no examples, no analysis of how description quality affects performance, and no sensitivity analysis for the alignment weight λ (Section 4.1, equation on line 66). Since the quality and specificity of these descriptions directly determines the alignment signal, this omission reduces reproducibility and interpretability.

- **ImLG's adversarial robustness at low perturbation strengths is worse than baseline**: The paper acknowledges that ImLG underperforms at low ε but outperforms at high ε (Section 5.4), interpreting this as evidence of "higher-level abstractions." An equally valid interpretation is that ImLG simply has different decision boundary geometry (e.g., smoother contours), which need not imply higher-level representations. The paper should discuss this alternative more thoroughly.

### Trivial
None.

## Nice-to-Haves

- **Random-initialization ablation for ImLG**: Replace the frozen LM block with a randomly initialized transformer of the same architecture. If performance is comparable, the "language" claim collapses for ImLG; if performance drops, it strengthens the paper significantly.

- **Alternative alignment targets for ExLG**: Compare alignment against non-linguistic structured embeddings (e.g., WordNet hierarchies, random orthogonal class representations) to determine whether language-specific semantics matter or whether any structured signal suffices.

- **Parameter-matched baseline**: Add an equivalent-parameter-count model (e.g., wider ResNet) to isolate the contribution of capacity from language-derived inductive bias.

- **Provide examples of class descriptions and λ sensitivity analysis**.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Claim that ImLG "does not involve language at all" and the paper's thesis "collapses"**: While the missing ablation is a serious gap, the harsh reviewer's assertion that ImLG provides *no* language guidance is itself unsubstantiated without the very ablation they call for. The paper cites Schwettmann et al. (2023) and Pang et al. (2023) for the hypothesis that text-trained transformers develop multi-modal neurons; this is a plausible (if untested) mechanism. The correct critique is that the claim is untested, not that it is definitively false. This was downgraded from "fatal" to "major."

- **CKA analysis is "circular" for CLIP-style models**: The reviewer claims Figure 1's CKA analysis is methodologically vague and potentially circular. The paper describes it as motivational (showing text representations are more similar across domains), not as proof. As a minor motivational figure, this is acceptable, and the paper does not hang its core claims on it.

- **"No additional data" claim is misleading for ImLG**: The reviewer argues this is misleading because the LM block was trained on massive text data. In context (Section 4.2), the paper means no additional multimodal data or joint training is required—only a frozen pretrained block is added. This is a reasonable framing for distinguishing from VLM approaches, not a misleading claim.

- **Cognitive science framing is "superficial decoration"**: While the connection between System 1/2 and ExLG/ImLG is loose, it serves as inspiration and terminology, not as a formal theoretical constraint. As long as the methods are clearly defined and evaluated, the framing is a presentation choice, not a scientific error.

- **Typo/various formatting issues**: Removed per instructions (parser artifacts).

- **Demand for proofs/theoretical guarantees**: Not standard for empirical papers of this type.

- **Demand for broader baselines in continual learning (DER++, DER)**: While desirable, the paper's scope is showing language guidance helps across multiple properties, not proposing state-of-the-art continual learning methods. The ER baseline is a standard reference point. Downgraded to a nice-to-have.

## Novel Insights

The分化 between ExLG and ImLG's behavior profiles—where ExLG excels in IID accuracy and continual learning stability while ImLG uniquely excels in OOD generalization and high-perturbation adversarial resilience—is a genuinely interesting empirical observation that suggests the two mechanisms operate through different inductive pathways. ExLG provides a direct constraint on representation geometry (align visual similarity structure to text similarity structure), while ImLG appears to regularize the visual feature space through the attention patterns learned from language data. However, without the random-initialization ablation, it remains unclear whether ImLG's benefits stem from language-specific priors or from architectural inductive bias, and the paper's strongest contribution (the differentiated behavior) is thus partially undermined.

## Suggestions

- **Run the random-initialization ablation**: Train ImLG with a random transformer block (same architecture, random initialization) and a vision-pretrained transformer block. This single experiment determines whether the paper's core claim about *language* guidance is valid for ImLG, and could transform the paper from suggestive to convincing.

- **Add a parameter-matched baseline** (e.g., wider ResNet-18) to demonstrate that ImLG's improvements are not simply due to increased capacity.

- **Tone down the ImLG narrative**: Instead of claiming ImLG "transfers abstract, high-level concepts from language," acknowledge that ImLG inserts language-initialized attention weights and that verifying whether the language origin matters is an open question (or resolved by the ablation).

- **Include examples of class descriptions and λ sensitivity curves** in ExLG to improve reproducibility and interpretability.

## Evaluation

**Originality**: The idea of using frozen language models in two distinct ways (explicit alignment vs. implicit architectural integration) to guide vision encoders is moderately novel. The ImLG approach—inserting a frozen LM attention block directly into the vision pipeline—is creative but currently unverifiable as "language guidance" rather than "language-initialized attention."

**Importance**: The research question (whether language priors can improve vision model robustness and generalization) is important and timely. The broad evaluation scope is a genuine contribution.

**Claims support**: The claims for ExLG are reasonably well-supported (language embeddings directly constrain visual representations). The claims for ImLG are substantially undermined by the missing ablation—the core mechanism attribution cannot be verified.

**Experimental soundness**: The experimental breadth is commendable but the experimental depth is lacking (no ablations for ImLG, no parameter-matched controls, limited baselines).

**Clarity**: The writing is generally clear, though the ImLG narrative overclaims relative to the evidence.

**Community value**: Even if ImLG's benefits turn out to be purely architectural, the empirical observation that language-initialized attention blocks improve OOD robustness and shortcut-learning resistance is valuable—provided the paper accurately characterizes the mechanism.

## Score and Decision

The paper addresses an important question with broad empirical evaluation and interesting results, but has a major gap: the ImLG contribution cannot be meaningfully evaluated as "language guidance" without a random-initialization ablation. This is not fatal—ImLG's results are interesting regardless—but the paper's central narrative is unsupported for half of its proposed methods. The missing ablation and parameter-matched controls are significant but addressable in revision.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>