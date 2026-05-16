Now I have a thorough understanding of the paper and can verify the reviewer's claims directly against the text. Let me synthesize the final review.

## Summary

The paper introduces "Cognition and Perception (C&P) knowledge conflicts" — a novel form of multimodal knowledge conflict in MLLMs where the cognitive (VQA) output does not match the perceptual (OCR) output from the same image region. The authors systematically measure these conflicts across five MLLMs and six document-understanding datasets, finding that even GPT-4o achieves only 68.6% C&P consistency. They propose a three-stage Multimodal Knowledge Consistency Fine-tuning method (Perception Consistency, Cognition Consistency, C&P Connector) that raises C&P consistency by 34–43 absolute percentage points across open-source models while generally maintaining or improving downstream task performance.

## Strengths

- **Novel problem identification.** The paper is the first to formalize and systematically measure C&P knowledge conflicts — inconsistencies between what an MLLM "sees" (OCR/perception) and what it "says" (VQA/cognition). The finding that even GPT-4o achieves only 68.6% consistency (Table 1) establishes the prevalence and severity of this issue, making a clear contribution to the field's understanding of MLLM reliability.

- **Large and consistent gains from the proposed method.** The three-stage fine-tuning improves C&P consistency by 34.83% (Qwen-VL-Chat), 37.85% (InternVL2-2b), and 43.19% (InternVL2-8b) — substantial absolute gains across different architectures and model sizes (Table 2). The ablation study (Table 4) confirms that the improvements are not driven by a single component, with the Perception Consistency task providing the largest contribution (14.79% average gain).

- **Broad evaluation scope.** The study covers 5 MLLMs (2 closed-source, 3 open-source across different architectures and scales), 6 document-understanding benchmarks (DocVQA, DeepForm, KLC, FUNSD, ChartQA, WTQ), and multiple metrics. This breadth strengthens the generality of both the problem characterization and the method's applicability.

- **Practical downstream benefits demonstrated.** Beyond consistency, Table 5 shows that the method improves or maintains cognitive (VQA) and perceptual (OCR) task performance in most model–dataset combinations, with particularly large gains in OCR (e.g., Qwen-VL-Chat's OCR ANLS jumps from 27.2% to 96.6% on ChartQA). This suggests the consistency gains translate to meaningful performance improvements.

## Weaknesses

### Fatal

None.

### Major

- **Lack of a controlled baseline for the additional training data.** The method uses 2.5M training samples (Stage 1: ~2,189K, Stage 2: ~176K, Stage 3: ~146K) drawn from the training splits of the same six datasets used for evaluation. The paper compares fine-tuned models only against the original untuned models (Table 2). Without a control condition where the same volume of data is used for standard supervised fine-tuning (VQA + OCR pairs without the consistency tasks), the observed improvements in C&P consistency cannot be cleanly attributed to the specific three-stage design. It is possible that much of the gain — particularly on OCR/perceptual tasks — comes from additional in-distribution training. This is the single most significant threat to the paper's causal claims about the method. The paper would be considerably stronger with such a control.

### Minor

- **The C&P consistency definition is narrow and tied to the evaluation construction.** The metric requires the VQA answer to be a substring of the OCR output (δ(y_C, y_P) = 1 iff y_C ⊆ y_P). This definition works by design only for extractive QA pairs whose answer appears literally in the OCR annotations. As the paper acknowledges, this filters out yes/no, comparative, and reasoning-derived questions (Section 2.2). The paper does not characterize how this filtering affects the difficulty distribution or answer properties of the evaluation set. While the scope is defensible for a first formulation, the gap between "substring match" and "cognition consistent with perception" as a general phenomenon should be acknowledged more explicitly.

- **Perceptual query format differs between closed- and open-source models in the initial evaluation (Section 3).** For closed-source models (GPT-4o, Qwen-VL-Max), the paper uses a red bounding box overlay (Set-of-Mark prompting) because the native bounding-box input format is unknown; for open-source models, the native format is used (line 136). No validation is reported to confirm that the red-box approach yields comparable OCR quality. This mainly affects the initial assessment (Table 1) rather than the method results (which use only open-source models), but it creates an uncontrolled variable in the closed- vs. open-source comparison.

- **The perceptual task evaluation uses ANLS while C&P consistency uses hard substring match.** Perceptual (OCR) task performance is reported with ANLS (character-level edit-distance tolerance), but C&P consistency demands exact substring containment. The paper does not report exact-match accuracy for the perceptual task, which would bridge these two metrics and help explain why C&P consistency remains far below 100% (e.g., Qwen-VL-Chat achieves 97.51% perceptual task ANLS but only 54.24% C&P consistency). This gap merits further analysis.

- **The three-stage ordering is not empirically justified.** The paper presents a fixed order (Perception Consistency → Cognition Consistency → C&P Connector) but the ablation study (Table 4) only tests presence/absence of each component, not their order. Given that the Cognition Consistency task adds only 0.44% average improvement beyond Perception Consistency + Connector (Rows 2 vs. 4 in Table 4), the necessity of having three separate stages and their specific ordering is not strongly supported. The paper acknowledges the Perception task dominates but does not discuss whether a simpler two-stage design would suffice.

- **Minor declines in cognitive task performance on some datasets.** Table 5 shows that InternVL2-8b's DocVQA score drops from 91.7% to 89.3%, and InternVL2-2b's DocVQA and ChartQA also decline. The paper acknowledges these as "minor" (line 341), but without a controlled baseline it is unclear whether these declines are inherent to the method or artifacts of the training setup (e.g., single-epoch training on imbalanced data).

- **No exact specification of the "small amount" of Stage 1/2 data reused in Stage 3.** Line 194 states Stage 3 includes "a small amount of data from previous stages" without quantifying it. This makes the training data composition partially opaque.

### Trivial

- The paper's formalization of knowledge subsets \(\mathcal{K}_C\) and \(\mathcal{K}_P\) (Section 2.1) is theoretically motivated but not operationalized in experiments — the paper measures response consistency, not knowledge subset overlap. A brief acknowledgment of this gap would improve clarity.

## Nice-to-Haves

- Add a controlled baseline: fine-tune each model on the same 2.5M samples formatted as standard VQA and OCR pairs (removing the consistency/connector tasks), then compare C&P consistency and downstream performance. This would isolate the effect of the specific method design from the effect of additional training data. This is the most impactful improvement the authors could make.
- Report exact-match accuracy for the perceptual (OCR) task alongside ANLS, to directly align with the C&P consistency metric.
- Characterize how the evaluation filtering (Section 2.2) affects distribution of question difficulty, answer length, and answer frequency.
- Include a small out-of-domain evaluation (e.g., scene-text dataset like ST-VQA) to test generalizability beyond document images.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The C&P Connector task explicitly trains the model to output the same text that appears in the bounding box... the reported improvements on this metric are partly circular."** — Removed because it mischaracterizes the C&P Connector. The connector is a two-option selection task (which bounding box contains the answer A?) that trains cross-task association between VQA answers and OCR bounding boxes (line 186: "TempQ_Conn(Q, Box, Box')" with "TempR_Conn(A, Box)"). It does not directly train substring matching or OCR output. The Perception Consistency task does train OCR, but improving OCR is a legitimate design goal, not a circularity. The paper is transparent about the relationship between the metric and the method.

2. **"The method's computational cost is not reported... The paper should compare compute investment against simpler alternatives."** — Removed as a nice-to-have that does not affect the paper's validity. Computational cost reporting is not standard for method papers of this type, and the paper's contribution is about consistency, not computational efficiency.

3. **"No evaluation on held-out datasets from a different domain"** — Moved to Nice-to-Haves because the paper acknowledges focusing on document understanding as a limitation (line 385-386). Expanding to other domains would make a stronger paper, but the current scope is a legitimate choice, not a flaw.

4. **"The case study does not provide a systematic analysis of failure modes"** — Removed because the case study (Figure 2) is presented as qualitative illustration, not as a systematic analysis. The paper does not claim otherwise.

5. **"The implementation details are sparse... no hyperparameter search"** — Removed. The reported details (lr=1e-5, batch size=128, 1 epoch, visual encoder frozen, 8 A100 GPUs) are standard and sufficient for reproduction. Single-epoch fine-tuning of 2.5M samples is common practice. Hyperparameter search is a nice-to-have, not a requirement.

6. **"The paper should report results separately on the filtered and unfiltered subsets"** — This is a reasonable suggestion but goes beyond what is standard for this type of analysis paper. Moved to Nice-to-Haves.

## Novel Insights

The reviews collectively surface a deeper tension in the paper: the C&P consistency metric and the proposed fine-tuning method are coupled in a way that makes disentangling "genuine cognition-perception alignment" from "better OCR" difficult. The Perception Consistency stage directly improves OCR quality, which mechanically raises C&P consistency (because better perceptual output makes substring match more likely). The Cognition Consistency stage adds almost nothing (0.44%), which suggests the main bottleneck is perceptual, not cognitive. This raises the question of whether the three-stage design is necessary or whether a simpler approach — improving OCR quality and adding a lightweight cross-task association — would suffice. The paper's strongest contribution is the problem formulation and measurement; the method, while effective, over-claims the novelty of its architecture. A controlled baseline separating "more data" from "better data organization" would resolve the central ambiguity.

## Suggestions

- **Add a single controlled baseline**: Fine-tune each model on the same 2.5M samples as standard supervised VQA+OCR pairs (without the GV consistency tasks or the connector). Compare C&P consistency. If the proposed method significantly outperforms this control, the core claim about the method's design is supported. If not, the paper should reframe the method as a data augmentation strategy rather than a novel consistency-enforcing mechanism.
- **Report per-dataset macro-averages** alongside micro-averages in the main results table, given the large variation in dataset sizes.
- **Provide exact-match accuracy for the perceptual task** to bridge the gap between ANLS-based OCR evaluation and the substring-based C&P consistency metric.
- **Quantify the "small amount" of Stage 1/2 data reused in Stage 3** and consider testing whether a two-stage variant (Perception Consistency + Connector, dropping Cognition Consistency) achieves comparable results.

## Score and Decision

The paper identifies a genuinely novel and important problem, provides a thorough measurement of its prevalence across current MLLMs, and proposes a method that yields large absolute improvements. However, the method evaluation is significantly weakened by the absence of a controlled baseline that isolates the effect of additional training data from the effect of the specific consistency tasks. Without this control, the causal attribution of improvements to the proposed design is uncertain. The problem definition and measurement contribution alone might suffice for acceptance at some venues, but the paper frames the method as a central contribution and its evaluation is incomplete.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>