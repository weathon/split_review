Now I have enough context to produce the final review. Let me write it.

---

## Summary

AtlasKV proposes a parametric method for augmenting LLMs with billion-scale knowledge graphs by (1) KG2KV, which converts KG triples into query-key-value training data with high attribute diversity, and (2) HiKVP, a hierarchical key-value pruning algorithm that reduces inference-time memory from linear to sub-linear complexity. The paper claims AtlasKV handles 1B triples under 20GB VRAM while achieving strong OOD generalization and outperforming KBLaM and ICL-based RAG.

## Strengths

- **Genuine scalability improvement over KBLaM**: HiKVP reduces time/memory complexity from $\mathcal{O}((M+N)ND)$ to $\mathcal{O}((C_t\sqrt[3]{M}+N)ND)$, and the paper demonstrates that AtlasKV with HiKVP stays under 20GB VRAM at scales where KBLaM exceeds 40GB. This is a meaningful contribution to making the parametric knowledge augmentation paradigm practical at scale.

- **KG2KV produces substantially more diverse training data**: Table 1 shows KG2KV achieves a 7.864% diversity ratio vs. 0.003% for the synthetic method used in KBLaM, with lower token cost. This is a concrete and well-motivated improvement over prior data construction approaches.

- **Strong OOD generalization evidence**: On ATLAS-Pes2o-QKV and ATLAS-CC-QKV — harder datasets with complex, diverse enquiry attributes — AtlasKV achieves dramatic improvements over KBLaM (e.g., 92.7% vs. 25.5% Top-1 at $10^2$ triples on ATLAS-Pes2o-QKV, Table 3). This validates the claim that KG2KV data diversity translates to better generalization.

- **HiKVP maintains accuracy under aggressive pruning**: AtlasKV with pruning settings (128-64-16) retains 90% Top-1 accuracy at $10^3$ triples on ATLAS-Pes2o-QKV compared to the unpruned variant (Table 3), demonstrating that the hierarchical retrieval design incurs only modest accuracy loss.

- **Well-designed ablation on entity types**: Table 4 convincingly shows that removing event entities or named entities from KG2KV training data causes significant accuracy drops, validating the design choice to include both.

## Weaknesses

### Fatal

None.

### Major

- **Figure 4 ICL memory curve contradicts the paper's own text and physics**: The paper states "when there are more than 100 triples in a KG, over 48GB VRAM is required" for ICL (Section 5.2), yet Figure 4 shows the ICL line remaining below 20GB from $10^4$ to $10^9$ triples. The ICL curve appears to reflect only static model weights without the KV cache and input embeddings that actual in-context learning would incur. This misrepresents AtlasKV's memory advantage over ICL and must be corrected. The paper cannot simultaneously claim ICL exceeds 48GB at 100+ triples and plot it below 20GB at all scales. This undermines the headline scalability comparison.

- **No comparison against a real retrieval-based RAG baseline**: The abstract and introduction position AtlasKV against the broad class of RAG systems, but the experiments include only ICL (full-context, no retriever), KBLaM, and zero-shot. A practical RAG baseline — e.g., a sentence-transformer retriever over textualized triples — is absent. Without this, the claim that AtlasKV provides "superior knowledge grounding" compared to RAG methods is unsubstantiated. This is the same limitation KBLaM was criticized for.

- **Training data confounds the KBLaM comparison**: AtlasKV is trained on KG2KV data while KBLaM uses synthetic data with much lower query diversity (Table 1). The paper attributes AtlasKV's performance gains to its method, but these gains are plausibly explained entirely by the richer training data. KG2KV is a contribution, but without training KBLaM on the same KG2KV data, the paper provides no evidence that AtlasKV's architectural modifications (dual-softmax attention, HiKVP) provide benefits beyond the better data. This weakens the claim that AtlasKV as a method is superior to KBLaM.

- **No evaluation on standard KG-QA benchmarks**: All evaluation datasets are constructed by the authors using the KG2KV pipeline. The paper does not test on established KG-QA benchmarks such as MetaQA, WebQSP, or SimpleQuestions. This limits confidence that AtlasKV's claimed benefits generalize to realistic, community-standard settings.

### Minor

- **CPU memory requirements unaddressed**: HiKVP keeps the full KV vectors on CPU and uploads only pruned subsets to GPU. For 1B triples with 384-dimensional embeddings, this would require order-of-terabytes of CPU RAM. The paper's headline "20GB VRAM" claim is technically accurate but omits the system-level memory footprint. This should be disclosed.

- **Knowledge-grounding metric justification is deferred to appendix**: The choice of the 15th layer for extracting attention scores is justified only in Appendix A.2 (stripped from this submission). The paper does report GPTScore (Figure 5) which correlates with answer quality, partially mitigating this concern, but the main results in Table 3 rely on the attention-based metric without in-text justification.

- **Undefined constants in complexity analysis**: Table 2 and the accompanying text introduce $C_t$ and $C_m$ as constants in the sub-linear complexity bounds, but their relationship to the top-k pruning values and hierarchical structure is never specified. Readers cannot evaluate the claimed scaling without this.

- **Offline clustering cost not discussed**: The hierarchical clustering requires UMAP + GMM on billion-scale embeddings. While the paper notes this is offline, the practical cost and feasibility boundary should be acknowledged.

### Trivial

- Figure 4 presents two sub-plots (ATLAS-CC-QKV and ATLAS-Pes2o-QKV) whose memory curves would be identical since memory depends on $M$ and architecture, not dataset content. This is redundant.
- Training set size (number of KGKV pairs) is not given, only the number of training steps.

## Nice-to-Haves

- Latency/throughput measurements: even with low VRAM, the multi-pass CPU-GPU data movement in HiKVP likely incurs latency that would be informative to report.
- Discussion of sentence encoder choice impact on retrieval quality.
- Analysis of how relation rewriting failures (for rare or ambiguous relations) affect the KG2KV pipeline.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The framing about 'no external retrievers' is misleading because HiKVP effectively performs a multi-stage retrieval"** — REMOVED. This is semantic hair-splitting. HiKVP operates within the attention layers using the model's own learned projections; it is not an external retrieval module in the RAG sense. The distinction the paper draws is valid.

- **"The paper fails to discuss CPU RAM required to store key-value vectors — roughly 3TB for 1B triples"** — PARTIALLY REMOVED (kept as Minor weakness rather than Major/Fatal). The paper's explicit claim is about GPU VRAM (title: "in 20GB VRAM"), and CPU RAM is a fundamentally different resource constraint. The harsh critic elevated this to a fatal flaw, which is disproportionate.

- **"The repeated memory curves in Figure 4 are confusing and unnecessary"** — DEMOTED to Trivial. This is a presentation nitpick.

- **"No latency or throughput measurements"** — MOVED to Nice-to-Haves. This is a desirable addition but not a weakness that threatens the paper's claim, which is about memory scalability, not speed.

- **"The ICL memory comparison is factually wrong"** — KEPT as Major but with verification. The contradiction between Figure 4 and the text is confirmed from the paper.

- **"Demand that the paper address problems outside its stated scope"** — REMOVED. The scope is KG augmentation; criticizing missing areas not promised is scope creep.

## Novel Insights

None beyond the paper's own contributions. The review process did not surface genuinely novel observations that the paper itself does not make; the key findings are confirmatory of the paper's strengths (KG2KV data diversity helps generalization, HiKVP enables sub-linear scaling) while identifying important evaluation gaps.

## Suggestions

- **Fix Figure 4**: Either show ICL with realistic memory costs (including KV cache) that would exceed the 48GB line at modest triple counts, or remove the ICL curve entirely and rely on the text to explain why ICL is infeasible. The current curve is misleading.
- **Add a KBLaM + KG2KV data ablation**: Train KBLaM on the identical KG2KV training data to isolate whether AtlasKV's performance gains come from data quality or architectural improvements.
- **Include at least one standard KG-QA benchmark** (e.g., MetaQA or WebQSP) and one practical RAG baseline to substantiate claims of superiority over retrieval-based methods.
- **Disclose CPU RAM requirements** for billion-scale deployment alongside the GPU VRAM numbers.
- **Define $C_t$ and $C_m$** in terms of the top-k pruning parameters and hierarchical structure.

## Score and Decision

**Round 1 bracket**: 4.0–6.0, based on comparison with KBLaM (5.80, accepted), SubgraphRAG (6.00, accepted), and weaker KV-cache papers (4.00–4.67).

**Round 2 narrowing**: AtlasKV is between "Knowledge Augmentation: In-context or In-parameter?" (5.50, rejected — limited novelty, evaluation gaps) and KBLaM (5.80, accepted — similar evaluation limitations but no Figure 4 issue). AtlasKV has more novel contributions than the 5.50 paper (KG2KV + HiKVP are both substantive) but has a concrete evaluation flaw (Figure 4 ICL curve) and lacks standard benchmarks. This places it at approximately 5.0.

**Anchor comparison summary**:
| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| KBLaM (aLsMzkTej9) | 5.80 | R1 | AtlasKV extends KBLaM with real improvements; has similar evaluation gaps plus the Figure 4 issue |
| SubgraphRAG (JvkuZZ04O7) | 6.00 | R1/R2 | Stronger evaluation with standard benchmarks; AtlasKV has more novel architecture but weaker validation |
| In-context or In-parameter (sl4hOq9wm9) | 5.50 | R2 | Similar tier; AtlasKV has more technical novelty but the Figure 4 issue is a concrete weakness |
| Running Huge Context (pG820nmDvy) | 4.67 | R2 | AtlasKV is clearly stronger — more novel method, better experiments |
| KV-Distill (p7vJ3wsm34) | 4.00 | R2 | AtlasKV substantially stronger |

The paper makes genuine contributions (KG2KV data construction, HiKVP hierarchical pruning) that advance the parametric KG augmentation paradigm. However, the Figure 4 ICL inconsistency, lack of standard benchmarks and RAG baselines, and confounded KBLaM comparison prevent the evaluation from supporting the paper's strong claims. The score reflects these mixed signals: real technical value offset by evaluation weaknesses that would need to be addressed in a revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>