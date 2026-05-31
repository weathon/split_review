Now I have enough context for calibration. Let me write the final consolidated review.

## Summary

This paper proposes a method to convert pre-trained autoregressive language models (GPT2, LLaMA2) into discrete diffusion language models (DLMs) via a continued pre-training recipe involving attention mask annealing, a shift operation, and a time-embedding-free architecture. The resulting models (DiffuGPT up to 355M, DiffuLLaMA at 7B) are evaluated on language modeling, reasoning, infilling, and unconditional generation tasks. The paper demonstrates that adaptation produces DLMs that outperform existing DLMs and scales diffusion models to 7B parameters for the first time.

## Strengths

1. **Gap-bridging adaptation recipe**: The paper introduces attention mask annealing (§3.3.1) and shift operation (§3.3.2) to align AR model architecture/objective with diffusion modeling. The ablation study (Table 4, referenced as tab:gsm) shows that removing either operation degrades GSM8K accuracy (e.g., "w/o shift" drops from 45.4 to 42.1 for GPT2-Small), providing causal evidence that these components are necessary for successful adaptation.

2. **First 7B diffusion language model**: The paper scales DLMs to 7B parameters (§4.1), far exceeding prior DLMs (e.g., Plaid 1B, SEDD-1B). In Table 1, DiffuLLaMA achieves state-of-the-art among all compared DLMs across nearly all tasks (e.g., HellaSwag 57.4 vs SEDD-1B 52.8, GSM8K 32.6 vs best prior DLM 26.0). This is the largest-scale demonstration of a text diffusion model and represents a genuine engineering and research contribution.

3. **Unified objective formulation**: Section 3.2 explicitly connects the discrete diffusion loss (Eq. 3) and the AR cross-entropy loss (Eq. 4), showing that AR is a special case of deterministic right-to-left masking diffusion. This theoretical grounding justifies why AR parameters can be transferred and why discrete diffusion (DD) outperforms continuous diffusion (CD) in adaptation (Table 4: DD accuracy 45.4 vs CD 32.3).

4. **Comprehensive evaluation beyond perplexity**: The paper evaluates on reading comprehension (TriviaQA), reasoning (GSM8K), commonsense (HellaSwag, Winogrande, PIQA, SIQA), and infilling tasks (§4.2). This addresses the limitation of prior DLM evaluations that relied almost entirely on zero-shot perplexity (criticized in §4.2).

5. **Inference speed advantage for long sequences**: Figure 5 shows that with T=256 denoising steps, DiffuLLaMA generates 1024+ tokens faster than LLaMA2 (using flash-attention 2), demonstrating a practical efficiency advantage for long-form generation.

## Weaknesses

### Major

1. **Uncontrolled comparison between DiffuGPT and GPT2 confounds the claimed AR-competitive result**: The paper claims "DiffuGPT outperforms GPT2 in most tasks" and that adapted DLMs are "competitive with their AR counterparts." However, GPT2 was pre-trained on WebText (~40GB) while DiffuGPT continues training on an additional 30B tokens from FineWeb, a different and improved corpus. The comparison does not control for training data: the improvement could stem entirely from the additional/better data rather than the diffusion modeling objective. To isolate the effect of the diffusion objective, the authors would need to compare against an AR model continue-trained on the same data. The ablation on GSM8K (Table 4) does control for data and shows DD loss outperforming AR loss, which supports the diffusion-specific benefit at the fine-tuning level, but the main pre-training comparison remains confounded. The paper acknowledges this issue only for DiffuLLaMA (line 209: "DiffuLLaMA's performance still falls short... presumably attributed to... insufficient training") but does not apply the same scrutiny to DiffuGPT vs GPT2. This is the paper's most significant weakness and undermines its headline claim.

2. **Mask annealing presented as a key contribution but abandoned for the 7B model**: The paper positions attention mask annealing as a central component of the adaptation method (§3.3.1, Figure 1). Yet for DiffuLLaMA (7B), the paper states they "directly use bi-directional attention without attention mask annealing" (line 184), with the justification that "mask annealing has minimal impact, so we choose to omit it for 7B adaptation" (line 250). This inconsistency weakens the narrative and raises questions about the actual contribution of mask annealing. While the ablation shows it has some effect on smaller models (45.4→44.0 for GPT2-small, 49.7→48.3 for GPT2-medium), the decision to skip it for the largest-scale demonstration means the full proposed method is not validated at scale.

### Minor

3. **The DiffuLLaMA in-context learning results are modest and overclaimed**: Section 4.4 discusses ICL and reasoning capabilities, but the results in Table 2 show small few-shot improvements, CoT that degrades performance, and self-consistency hit rates indicating high uncertainty. The paper's framing — "is capable of following in-context demonstrations to some extent" — is more measured than the harsh critic suggests, but the surrounding language in the abstract and introduction ("exhibiting in-context learning") overstates the evidence, which shows mostly small improvements from 0-shot to few-shot and a 3-shot majority-vote accuracy of only 5.5 on GSM8K-symbolic.

4. **Mask annealing schedule is underspecified**: The paper states "At each training step, we sample the amount of context from the right side and progressively increase this amount till we obtain the full attention mask" (line 148) but gives no details about the schedule (linear? cosine? step function?), duration, or ratio progression. For a central claimed contribution, this lacks the specificity needed for reproducibility.

5. **Time-embedding-free design lacks ablation**: The paper asserts that timesteps can be learned implicitly from mask count (citing prior work) and omits time embeddings. However, no ablation tests whether performance degrades without them in this specific setting. Given that this is a design choice differentiating the approach from most prior DLMs, an ablation would strengthen the paper.

6. **Inference speed benchmark is limited**: The speed comparison (Figure 5) uses only batch size 1. In batch settings, the throughput dynamics may differ, and the practical advantage of diffusion models for batched generation needs more thorough benchmarking.

### Trivial

None.

## Nice-to-Haves

- A controlled AR baseline continue-trained on the same data (e.g., FineWeb) would cleanly isolate the effect of the diffusion objective and substantially strengthen the core claim.
- Reporting GPU-hours for full-parameter fine-tuning at 7B would help practitioners evaluate the method's practicality.
- The infilling comparison notes "we do not provide the suffix information to the model, which might result in an unfair comparison" (line 213). This is properly acknowledged but could be more clearly flagged in the table.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. *"The shift operation is presented as a natural consequence when it is actually a heuristic"* — The paper explicitly justifies it as addressing input-output misalignment (lines 150-152) and validates it via ablation (Table 4). It is not presented as a formal proof but as an empirically motivated technique, which is appropriate for an empirical systems paper. **REMOVED** — factually grounded but mischaracterizes what the paper claims.

2. *"The paper overclaims the capabilities of DiffuLLaMA"* — The paper's own language at line 239 ("we show the potential capabilities") and lines 235-238 (acknowledging CoT degradation and the need for instruction tuning) is cautious rather than overblown. The abstract/claims language is somewhat stronger, but the evidence section is measured. **REMOVED** — partly addressed in weakness #3 above in a more precise form.

3. *"Unconditional generation is a clean comparison among DLMs but does not address the AR comparison"* — This is an observation, not a weakness. The paper doesn't claim it addresses the AR comparison. **REMOVED** — not a weakness.

4. *"The ablation on GSM8K is a small-scale proxy and may not transfer"* — The paper acknowledges this limitation explicitly (line 244: "Direct ablation on adaptation training is costly; hence, we conduct preliminary experiments"). It is a standard practice and properly caveated. **REMOVED** — creates a standard of evidence not required by the paper's scope.

## Novel Insights

The harsh critic's observation about the data confound is the key insight that goes beyond what the paper itself acknowledges: while the authors note that DiffuLLaMA underperforms LLaMA2 due to insufficient training, they do not extend the same scrutiny to the DiffuGPT vs GPT2 comparison, where the same confound applies. This asymmetry in self-criticism is a genuine oversight that a reader could miss. The strength finder independently identifies the unified objective formulation (Section 3.2) as a novel connection — showing AR as a special case of deterministic masking diffusion — which is a genuinely useful theoretical contribution that the paper positions as a bridge rather than a standalone result. Together, these suggest the paper's strongest framing is as a method for building better DLMs via adaptation, not as a demonstration that DLMs match AR models.

## Suggestions

1. **Fix the data confound**: Add a controlled AR baseline trained on the same FineWeb/SlimPajama data used for DiffuGPT/DiffuLLaMA, or at minimum reframe the headline claims to focus on the DLM-vs-DLM comparison. The claim "DiffuGPT outperforms GPT2" should be caveated to "under additional training data."

2. **Acknowledge the mask annealing inconsistency explicitly**: State clearly that mask annealing is primarily useful for smaller models and that the 7B adaptation succeeds without it, and discuss what this implies about when the technique is needed.

3. **Provide mask annealing schedule details** (e.g., "linear increase from 0% to 100% right-context over 10K steps") for reproducibility.

4. **Add an ablation for the time-embedding-free design**, even on a small-scale proxy task, to confirm the implicit timestep inference works as claimed.

5. **Tone down the AR-competitive language** in the abstract/introduction unless the controlled baseline experiment is added.

## Score and Decision

**Score bracketing and calibration**:
- **Round 1 bracket**: [4, 7]. Weak anchors (score ≤3) were irrelevant diffusion papers in non-text domains. Middle anchors (4–7) included continued pre-training and adaptation papers. Strong anchors (8+) included SAR diffusion and theoretical discrete diffusion papers.
- **Round 2 narrowing**: Compared against "Scaling up Masked Diffusion Models on Text" (6.50, accepted), "Diffusion Language Models Can Perform Many Tasks with Scaling" (5.00, rejected), "Discrete Diffusion Language Modeling by Estimating Ratios" (6.60, rejected), and "Adapting LLMs via Reading Comprehension" (6.50, accepted).
- **Final anchoring**: The paper is clearly stronger than the 5.00 rejected paper (which had no method contribution and used existing RDM). It is comparable to the 6.50 accepted papers — it has a genuine method contribution and scales to 7B but is weakened by the data confound. It is weaker than the 8.00 SAR paper (which had a novel model class with rigorous theory). The paper sits at **6.0**: solid borderline accept with clear contributions and fixable weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>