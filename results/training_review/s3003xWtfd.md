Now I have thoroughly verified the paper content against the reviewer's claims. Let me produce the final consolidated review.

## Summary

CoreInfer proposes an MLP-free adaptive sparse activation method for LLM inference. Instead of predicting which neurons to activate per-token using additional MLP predictors (as in DejaVu, PowerInfer), the paper defines **sentence-wise core neurons** — the most frequently activated neurons across all tokens in a sentence — and determines these once during pre-filling, then reuses them throughout decoding. The paper empirically discovers that core neurons exhibit **stability** (changing little when semantics are stable) and **similarity** (sentences on the same topic share core neurons), and uses these insights to design two prediction strategies (stability-guided for long fluent inputs, similarity-guided for short/unstable inputs). Experiments across OPT, LLaMA2, and LLaMA3.1 on six tasks show speedups of up to 10.33× on TITAN XP and 2.3× over PowerInfer on A100, with modest performance changes.

## Strengths

1. **MLP-free sentence-level sparsity eliminates predictor overhead during decoding.** Unlike prior token-wise methods (DejaVu, PowerInfer) that insert an MLP predictor per layer, CoreInfer predicts activated neurons once at pre-filling and never changes the activation map during decoding. Table 3 confirms CoreInfer has 0 ms predictor latency and 0 GB predictor memory, while DejaVu requires 9.62 ms/1.85 GB and PowerInfer 15.96 ms/3.36 GB — a clean architectural advantage.

2. **Empirical discovery of core-neuron stability and semantic similarity is novel and well-motivated.** Section 3.2 demonstrates that (a) adding 8 tokens to a 256‑token sentence changes core neurons by only 3% when semantics are stable, and (b) sentences from the same topic (ag news) form clear clusters in core-neuron space (Fig. 4). These observations are prior-unaware and directly enable the two prediction strategies.

3. **Meaningful speedups across model families and hardware.** On an NVIDIA TITAN XP with OPT‑6.7b, CoreInfer achieves 19.83 tokens/s (10.33× over Huggingface, 2.71× over PowerInfer). On A100 with LLaMA2‑70b, it reaches 17.2 tokens/s (5.5× over Transformer, 2.3× over PowerInfer). The speedups are demonstrated across ReLU‑based OPT and SiLU‑based LLaMA models, showing generality.

4. **Validation of core-neuron effectiveness beyond ReLU activations.** Table 1 reports Spearman correlations between core-neuron similarity and semantic similarity on STS‑B and SICK for both ReLU‑based OPT (0.52–0.56) and SiLU‑based LLaMA2/3.1 (0.65–0.66), demonstrating the phenomenon is not activation-function-specific.

5. **Memory reduction is a practical benefit.** CoreInfer reduces OPT‑6.7b GPU memory from 12 GB (Transformer/DejaVu) to 7.28 GB, enabling the model to fit entirely on a 12 GB TITAN XP and eliminating CPU‑GPU transfers. This memory efficiency is directly attributable to the sentence-level static activation strategy.

## Weaknesses

### Fatal
None.

### Major

1. **The similarity-guided prediction method is critically underspecified, making the zero-shot results non-reproducible.** Section 4 states: "we cluster the training dataset based on this similarity… Once the input sentence's group is determined, its core neurons are identified by selecting the top γ neurons that appear most frequently within that semantic group." The paper never specifies: (a) what clustering algorithm is used, (b) how many clusters, (c) how a new input sentence is assigned to a group (nearest centroid? threshold?), (d) what dataset the groups are built from (the downstream training set?). For a method that claims to handle zero-shot scenarios where stability fails, this lack of detail is a significant gap — a reader cannot reproduce the results or assess the offline cost. This is the single most significant weakness in the paper.

2. **The headline speedup numbers on TITAN XP conflate memory-residency benefits with sparsity-computation benefits.** On the TITAN XP, OPT‑6.7b (~13 GB in FP16) does not fit on the 12 GB GPU, so the Transformer baseline (1.92 tokens/s) must offload to CPU. CoreInfer uses only 7.28 GB and fits entirely on GPU (19.83 tokens/s). The resulting 10.33× speedup reflects both (a) avoiding CPU‑GPU transfers and (b) reduced computation from sparsity. These are not cleanly separated. While the A100 results (Fig. 7) partially address this (e.g., LLaMA2‑7b fits entirely on A100 for all methods), the paper does not report the *sparsity ratio* per layer for each method or provide a controlled comparison at the same active-neuron budget. A fair assessment of the sparsity-specific benefit requires an experiment where both CoreInfer and baselines use the same number of active neurons per layer, or at minimum a statement of what fraction of neurons each method activates.

### Minor

3. **The claim of "without degrading task performance" is unsupported by statistical analysis.** Table 2 reports single-run values without confidence intervals or significance tests. Several entries show noticeable drops (e.g., OPT‑6.7b Xsum ROUGE 6.7→6.3; LLaMA2‑7b SQuAD 50.8→49.2; LLaMA3.1‑8b SQuAD 54.3→49.7). While many differences are small, the paper also reports occasional *improvements* (e.g., TruthfulQA BLEU max 23.6→23.8), which may reflect noise rather than genuine "more specialized neurons." Without variance estimates or significance tests, the paper's central claim of lossless acceleration is not rigorously supported.

4. **The stability assumption for decoding is only tested on coherent continuations, not on diverse generation scenarios.** The stability experiment (Section 3.2) adds fluent continuations to existing sentences — a setting where semantics remain almost perfectly aligned (semantic similarity ≈ 1). This is a reasonable proxy for summarization and few-shot tasks, but the paper does not test whether core neurons from the prompt remain appropriate when the model generates semantically divergent content (e.g., multi-turn dialogue, creative writing). However, this limitation is partially mitigated by the use of similarity-guided prediction for "unstable" inputs and by the fact that the evaluated tasks produce relatively short outputs.

5. **The pre-filling cost is not quantified.** CoreInfer determines core neurons by analyzing activations from the pre-filling forward pass. While the marginal cost of frequency counting is small, the paper neither measures this overhead nor discusses its impact for very short generations (e.g., single-word answers) where pre-filling could dominate. The "zero-cost sparse inference" claim in the abstract is specific to the decoding stage but is ambiguous without this qualification.

### Trivial
- In Table 2, the column header "wmnt16-ro-en" contains a typo ("wmnt" instead of "wmt").
- The reference to "encoding stage" in the abstract appears to mean "decoding stage."

## Nice-to-Haves
- A controlled sparsity experiment: compare CoreInfer to a variant of DejaVu/PowerInfer constrained to the *same* active-neuron ratio per layer. This would isolate the benefit of CoreInfer's prediction quality from memory-fit effects.
- A long-form generation evaluation (e.g., story generation, long-document summarization with outputs >512 tokens) to test whether the stability assumption holds over extended decoding.
- An analysis of core-neuron overlap between prompt tokens and generated tokens — compute Jaccard similarity between (a) core neurons from the pre-filling stage and (b) the actual core neurons of each generated token, to directly measure whether stability holds during autoregressive generation.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The similarity-guided method is not MLP-free"** — The paper's "MLP-free" claim refers specifically to not adding per-layer MLP predictors to the LLM during inference (Table 3 compares predictor latency/memory). Using Sentence-BERT for *offline* group construction does not contradict this claim; the paper never asserts that no external models are used anywhere in the pipeline. REMOVED (misinterprets the paper's scope).

2. **"Pre-filling cost is comparable to or greater than MLP predictors"** — This is factually incorrect. The pre-filling forward pass already executes during standard inference; CoreInfer piggybacks on it with a lightweight frequency analysis. MLP predictors add extra forward passes per layer for *every decoding token*, a far larger cost. The paper could quantify this cost, but the critic's equivalence claim is wrong. REMOVED (factually incorrect).

3. **"No experiment showing core neurons from input remain appropriate for generated tokens"** — The stability experiment (Fig. 3/Fig 4 in paper) directly tests this by adding tokens to a sentence and measuring core-neuron similarity. The paper does test this, albeit with coherent continuations rather than arbitrary topic shifts. REMOVED (contradicted by paper content).

4. **"The paper's motivation to avoid 'frequent changes in activation maps' is partially contradicted by the pre-filling computation"** — No contradiction exists. The paper avoids *decoding-stage* changes in activation maps (requiring repeated MLP calls). Pre-filling computation is a one-time cost. REMOVED (misunderstands the architecture).

## Novel Insights

The most insightful observation across the reviews is that the paper's central problem — validating whether core neurons from the prompt remain appropriate for autoregressively generated tokens — could be directly tested by computing the Jaccard overlap between (a) the pre-filling core neurons and (b) the actual core neurons of each generated token, and plotting this overlap over decoding steps. This simple experiment would either confirm the stability assumption or precisely quantify its failure modes (e.g., which layers, which generation steps, which tasks). The paper's current stability evidence (adding tokens to sentences) is a reasonable proxy, but a direct trace over actual generation would be much more convincing and could reveal whether periodic re-computation (e.g., every K tokens) is needed — a concrete extension the paper does not explore.

## Suggestions

1. **Specify the similarity-guided prediction method in full detail.** Provide the clustering algorithm, number of clusters, group assignment procedure, and the dataset used to build the groups. Without this, the zero-shot results cannot be reproduced.

2. **Report sparsity ratios and a controlled speedup comparison.** Report the fraction of neurons activated per layer for each method, and include an experiment where all methods use the same active-neuron budget to isolate prediction-quality benefits from memory-fit benefits.

3. **Add confidence intervals or standard deviations to Table 2.** Multiple inference runs (e.g., 3–5 seeds) would allow statistical comparison and validate the claim of "no degradation."

4. **Discuss pre-filling overhead explicitly.** Provide a breakdown of end-to-end latency showing pre-filling time vs. decoding time, particularly for short-output tasks.

5. **Include a direct overlap analysis** between pre-filling core neurons and the actual core neurons of each generated token, to directly validate the stability assumption during autoregressive generation.

## Score and Decision

The paper presents a genuinely novel idea (sentence-level sparsity without MLP predictors) and backs it with interesting empirical discoveries about core-neuron stability and semantic similarity. The reported speedups, while partially confounded by memory effects, are meaningful. However, the similarity-guided prediction method is critically underspecified (making the zero-shot results non-reproducible), and the claim of lossless acceleration is not statistically supported. These are significant but addressable weaknesses. The paper would benefit from major revisions and additional experiments before it is ready for publication.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>