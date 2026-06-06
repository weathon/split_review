## Summary
The paper introduces MISINFOTASK, a 108-task dataset designed to evaluate multi-agent system (MAS) robustness against misinformation injection, and ARGUS, a two-stage training-free defense framework that combines topology-aware critical flow localization with goal-aware CoT-based persuasive rectification. Experiments across four LLMs (GPT-4o-mini, GPT-4o, DeepSeek-V3, Gemini-2.0-flash), three injection methods, and five MAS topologies consistently show that ARGUS outperforms Self-Check and G-Safeguard baselines, achieving an average 28.17% reduction in Misinformation Toxicity (MT) and a ~10.33% improvement in Task Success Rate (TSR).

---

## Strengths

- **Consistent empirical results across all tested conditions (Table 1):** ARGUS achieves the lowest MT and highest TSR in every LLM × attack-type cell of Table 1, a pattern that holds across GPT-4o-mini, GPT-4o, DeepSeek-V3, and Gemini-2.0-flash. For example, average MT drops from 5.22 → 3.43 for GPT-4o-mini and from 4.12 → 3.40 for Gemini-2.0-flash. The within-run standard deviations (e.g., TSR std. devs of 0.12, 1.38, 0.30 per attack type for GPT-4o-mini with ARGUS) are small, confirming reproducibility across the three independent trials per condition.

- **Ablation study validates each component's contribution (Tables 2 and 3):** Removing dynamic localization raises MT from 3.50 → 4.55 (Prompt Injection), removing CoT Revision raises it to 3.90, and removing multi-turn correction raises it to 4.63, all confirmed on the same test set. Table 3 further shows that information relevance (γ) is the most important localization factor (MT 3.73 → 4.59 when removed), and optimal performance requires all three components jointly.

- **Topology robustness (Figure 6):** DeepSeek-V3 experiments over Chain, Full, Self-Determined, Circle, and Star topologies all show ARGUS reducing MT under every attack type tested, indicating the defense is not architecture-specific.

- **Temporal mitigation evidence (Figure 5):** Round-by-round MT trends show that without ARGUS, MT monotonically increases from ~4.5 to ~5.2 over 5 rounds, while with ARGUS it decreases (e.g., PI+ARGUS from ~4.5 to ~3.2), confirming active propagation curtailment rather than one-time blocking.

- **Well-defined dataset construction methodology (Section 3.1):** MISINFOTASK provides seed-example-guided construction with explicit quality criteria (factual pertinence, task relevance, category coverage) and offers 4–8 fallacious arguments plus ground truths per task, filling an identified gap in MAS misinformation benchmarks.

---

## Weaknesses

### Fatal
None.

### Major

- **Small dataset limiting statistical reliability of per-condition comparisons:** MISINFOTASK contains 108 tasks. When split across three attack types (~36 per condition), the MT and TSR numbers in Tables 2 and 3 each represent approximately 36 tasks. Small per-cell sample sizes mean that observed differences of 1–2 MT points or 3–5 TSR percentage points (e.g., "w/o CoT Revision" vs. full ARGUS: MT 3.90 vs. 3.50 for PI, Table 2) are difficult to evaluate without significance tests. The paper reports within-run std devs that are small (indicating stable runs), but no confidence intervals or significance tests are provided for the between-method comparisons. Expanding the dataset or reporting significance statistics would substantially strengthen the evidential basis for the component-level claims in Table 2.

- **Mismatch between dataset construction categories and goal-accuracy analysis (Figure 4 vs. Section 3.1):** Section 3.1 describes five explicitly named categories—Conceptual Reasoning, Factual Verification, Procedural Application, Formal Language Interpretation, and Logic Analysis—as coverage criteria for MISINFOTASK construction. Figure 4, which reports goal-inference accuracy, displays four unnamed categories (represented only by icons: person, globe, globe-with-cross, star). The paper provides no mapping between these four icon-labeled categories and the five construction categories, making Figure 4 difficult to interpret and leaving the category-level analysis disconnected from the dataset design.

### Minor

- **Goal inference accuracy described as "high" but reaching ~0.50 in some conditions:** Section 5.2 claims the adaptive module "successfully identified the misinformation's guiding direction with high accuracy," but Figure 4 shows accuracy as low as ~0.50 for the star-icon category under Tool Injection and ~0.55 for two categories under RAG Poisoning. At ~50% accuracy, goal inference is near chance for some conditions. The paper does not analyze whether the downstream defense performance degrades in these lower-accuracy conditions relative to higher-accuracy ones, leaving open how much the adaptive re-localization contributes under poor goal inference.

- **Figure 5 does not specify which LLM produced the temporal trends:** Given the substantial across-LLM variation in Table 1 (e.g., DeepSeek-V3 Attack-only Avg. MT = 4.59 vs. GPT-4o-mini = 5.22), Figure 5's generalizability is unclear. Specifying the LLM would allow readers to contextualize the curves.

- **In-scope misinformation definition creates a known evaluation boundary (acknowledged but underexplored):** Section 2.3 defines misinformation as "content that contradicts the factual knowledge implicitly stored in the parameters of an LLM," and Section 7 acknowledges this limits ARGUS to knowledge already resident in the model. The gap between ARGUS's performance and the Ground Truth upper bound in Table 2 (e.g., MT 3.50 vs. 3.32 for PI) could arise from knowledge gaps, goal misidentification, or persuasion failures—but the paper does not decompose these sources of failure. Characterizing where ARGUS falls short of GT would make the mechanism's actual capability more concrete.

- **LLM-as-judge applies the same model family (GPT-4o-2024-08-06) for evaluating agents that include GPT-4o/GPT-4o-mini:** While the judge evaluates all methods identically (which prevents direct bias toward ARGUS), there is an unacknowledged possibility that the GPT-4o family judge may implicitly rate GPT-4o-family-generated corrections more favorably in style or phrasing. A cross-family judge comparison (e.g., using DeepSeek or Gemini as judge) or acknowledgment of this potential confound would strengthen the evaluation.

### Trivial

- **The threshold θ_m is described as "predefined" in Eq. 1 without stating its value in the main text.** Since TSR is a binary threshold metric, its specific value directly shapes the headline TSR numbers and comparisons; the value should appear in Section 3.2, not only in the appendix.

- **The hyperparameter k (number of monitored edges) is used in Eq. 4 and Eq. 9 but its selection criterion is not stated in the main body.** The ablation covers the weights α, β, γ but not k itself.

---

## Nice-to-Haves

- A mechanistic failure case: showing one concrete example where ARGUS fails to correct misinformation (and why—knowledge gap, goal misidentification, or failed persuasion) would ground the limitations section and make the claims more credible by demonstrating the authors understand the method's boundary conditions.

- A rough token-count or wall-clock overhead comparison between vanilla MAS and ARGUS-augmented MAS, even approximate, would help practitioners assess deployment cost. Section 7 notes computational overhead qualitatively but provides no numbers.

- Validation that the four icon-labeled categories in Figure 4 map onto the five named categories in Section 3.1 (or a clarification that they are different dimensions), which would connect the dataset's design criteria to the empirical accuracy analysis.

- A cross-family judge check (e.g., re-evaluating a subset using DeepSeek or Gemini as judge) to rule out model-family preference in the automated scoring.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic — "11% Avg. TSR std dev makes headline numbers untrustworthy" (as framed as structural):** After inspection, the 11.00% value in Table 1 is the standard deviation *across attack types* (PI: 75.86, RP: 69.77, TI: 89.66), not across independent runs. Within-run std devs for TSR are 0.12, 1.38, and 0.30 respectively—very small. The high cross-attack variance is expected and substantively meaningful (Tool Injection allows easier correction than RAG Poisoning), not a sign of statistical instability. The concern about dataset size is retained as Major, but the framing that the 11% std dev "swamps" the evidence is incorrect and removed.

- **Harsh critic — "circular LLM-as-judge evaluation is structural and affects every result simultaneously":** The GPT-4o-2024-08-06 judge is applied uniformly to all methods (Attack-only, Self-Check, G-Safeguard, and ARGUS) and all four underlying LLMs. There is no demonstrated systematic advantage to ARGUS from this setup; the risk is a generic evaluation preference, not a directional bias toward ARGUS specifically. Downgraded to Minor with a note about cross-family validation.

- **Harsh critic — "tautological evaluation approaching structural":** The paper explicitly states this scope in Section 2.3 and acknowledges it in Section 7 as a limitation. Evaluating a method within its own stated scope is not a flaw; it is appropriate scoping. The concern that this limits the conclusions is valid but is already disclosed, and does not undermine the within-scope claims. Retained only as Minor.

- **Strength Finder — "accurate goal inference enables re-localization" (framed as a core strength at 0.55–0.80):** Accuracy in the 0.50–0.55 range for some categories is not "high accuracy." This framing conflicts with the verified Figure 4 data and is removed as a strength. The temporal and topology robustness strengths are retained as better-grounded evidence.

---

## Novel Insights

The paper's most novel architectural insight is the combination of graph-theoretic edge betweenness centrality for initial localization (without requiring interaction logs) with dynamically updated semantic relevance scoring based on inferred misinformation goals for subsequent rounds. This allows the defense to bootstrap from graph structure alone and then refine in real time—a principled two-phase design that neither G-Safeguard (static GNN) nor Self-Check (uniform self-reflection) can replicate. The ablation evidence that information relevance (γ) is the dominant localization factor (MT jumps to 4.59 without it vs. 3.73 full system, Table 3) while topological importance (α) provides the essential cold-start signal (MT jumps to 4.14) is a concrete, quantified observation about the relative value of graph-prior vs. semantic-posterior knowledge in adversarial localization.

---

## Suggestions

1. Expand MISINFOTASK or run significance tests: add a bootstrap or permutation test on the between-method MT/TSR differences in Tables 1–2 using the 3-run results, or expand to at least 200–250 tasks to support more robust per-condition conclusions.
2. Explicitly map or reconcile the five construction categories (Section 3.1) with the four icon-based categories in Figure 4, or use named labels in Figure 4 to maintain consistency.
3. State θ_m and k with justification in the main body (Section 3.2 and Section 4.1 respectively).
4. Run one cross-family judge experiment (e.g., use Gemini-2.0-flash as judge) on a representative subset to address the same-family evaluation concern.
5. Decompose the Ground Truth gap in Table 2 (e.g., for PI: MT 3.50 ARGUS vs. 3.32 GT) into failure modes: knowledge gap, goal misidentification, or persuasion failure—even for a subset of tasks.

---

## Evaluation on Key Axes

- **Originality:** The combination of graph-centrality localization with goal-aware LLM-intrinsic correction applied specifically to misinformation (as distinct from jailbreak) in MAS is novel. The dataset MISINFOTASK addresses a real gap. Score: **Moderate-High**.
- **Importance:** Misinformation robustness in agentic systems is a timely and underexplored problem with direct practical relevance. Score: **High**.
- **Claims supported:** Core claims (ARGUS consistently outperforms baselines) are supported by consistent evidence across multiple models, topologies, and runs. Fine-grained claims (component-level MT differences of 0.3–1 point with n~36) are less firmly grounded. Score: **Moderate**.
- **Soundness:** The methodology is principled and appropriately scoped, with the key limitation (in-LLM-knowledge scope) acknowledged. The evaluation setup has minor confounds (same-family judge) but is defensible. Score: **Moderate**.
- **Clarity:** Generally clear, with well-illustrated figures. Some gaps: Figure 4 category labels, Figure 5 missing LLM specification, k and θ_m deferred from main text. Score: **Moderate**.
- **Community value:** Both the dataset and the framework are releasable artifacts with practical value for MAS security research. Score: **High**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>