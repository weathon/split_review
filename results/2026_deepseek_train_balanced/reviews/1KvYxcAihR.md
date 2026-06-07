## Summary

TMGBench introduces a benchmark for evaluating LLMs' game-theoretic reasoning that systematically covers all 144 game types from the Robinson-Goforth topology of 2×2 ordinal games — a principled, exhaustive taxonomy rather than the ad-hoc selection of 3–5 canonical games seen in prior work. The benchmark also provides story-based variants (generated via GPT-4o with topic guidance and human inspection) to mitigate data leakage, and it composes atomic games into sequential, parallel, and nested forms for scalable evaluation. Experiments across 8 LLMs with multiple prompting strategies (DA, CoT, FoToM, SoToM) reveal that top models achieve ~80% accuracy on classic games but show sharp degradation on story-based variants, asymmetric error patterns on 0-equilibrium games, and limited success on complex forms (o1-mini at 66.6%, 60.0%, 70.0%).

## Strengths

- **Exhaustive coverage of all 144 game types from the Robinson-Goforth topology (Section 2.2, lines 88–97):** Prior work tests only a handful of games (Prisoner's Dilemma, Battle of the Sexes, Stag Hunt, etc.), but TMGBench systematically incorporates every equivalence class in the 12×12 topology. This provides a principled, complete sampling of 2×2 game structures rather than ad-hoc selection, directly addressing the limited-coverage limitation that motivates the paper.

- **Synthetic data pipeline with topic guidance and human inspection for story-based games (Section 2.3, lines 99–112):** Five contextualized variants per classic game are generated using GPT-4o with explicit quality controls (precise prompts, topic selection from business/law/transportation, human review). The subsequent evaluation validates the approach: top models' S-PAR₂ drops to less than one-third of C-PAR₂ (line 240), confirming that story-based games are nontrivial, not surface-level rewrites.

- **Complex game forms (sequential, parallel, nested) built from atomic game units (Section 2.4, lines 132–141):** Treating individual 2×2 games as atomic units and composing them into three organizational structures provides a natural path toward harder tasks. Empirical results confirm the framework's value: o1-mini achieves only 66.6%, 60.0%, and 70.0% on sequential, parallel, and nested forms respectively (line 284), demonstrating that the benchmark can challenge state-of-the-art reasoning models.

- **Novel bias metric exploiting the topological symmetry of the Robinson-Goforth framework (Section 2.5, lines 161–168):** The Bias Degree (BD) quantifies whether LLM responses break the counter-diagonal symmetry inherent in the topology — effectively measuring whether swapping player identities changes the model's answers. This reveals a non-coincidental asymmetric pattern in GPT models on 0-task games (lines 274–277) that would be invisible to accuracy-only metrics.

- **Controlled comparison of first-order and second-order ToM prompting across multiple models (Section 3.2, lines 247–253):** The paper systematically tests FoToM and SoToM on 8 models with per-task-type results. The finding that Llama-3.1-70B shows first-order but not second-order ToM ability, and that SoToM improvements generally do not exceed FoToM, is a specific empirical contribution about ToM capability boundaries.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Lack of empirical comparison against GTBench:** The paper cites GTBench (Duan et al., 2024) in the related work (line 297) and motivates TMGBench by citing limitations of prior work (limited coverage, data leakage, poor extensibility), but never empirically compares the two benchmarks. For a benchmark paper, the reader cannot assess whether TMGBench yields different or deeper insights than existing tools. An ablation showing that rankings based on only a subset of game types (those in prior benchmarks) would produce unreliable conclusions would directly validate the paper's main motivation. This is the most significant gap.

- **Small effective sample sizes limit quantitative precision:** With 4 tests per data point (line 187), a single trial flip changes PAR by 25 percentage points. For story-based settings, 5 instances per game type (line 106) with error bars over 5 data points provide limited statistical power (line 221 caption). The complex forms use only 20 runs per configuration (line 267), yet the paper reports figures like "66.6%" to one decimal place without confidence intervals. While temperature ~0 reduces variance, the precision reported is not warranted by the sample sizes, and this limits the reliability of inter-model comparisons and claims about specific performance degradation magnitudes.

- **Response format and parsing pipeline are underspecified:** The paper states that the LLM's response should contain "a list of choices corresponding to multiple choices or no choice (when the given list is empty)" (line 144) and maps choices to four quarter-grid positions (line 147). However, the exact prompt template used, how "no choice" is elicited and parsed, and what happens when the model returns free-form text rather than structured output are not described. This hinders reproducibility and is particularly relevant for 0-task games where the expected output is "no equilibrium."

- **Story-based games are generated by GPT-4o, creating a potential confound when GPT-4o is evaluated on them:** The paper uses GPT-4o to generate story-based narratives (line 104), and then evaluates GPT-4o (and other models) on those narratives. Models that share GPT-4o's narrative conventions or framing biases may systematically appear better at "reasoning" about these scenarios. The paper does not acknowledge this confound. While the empirical results partially mitigate the concern (gpt-4o-mini sometimes outperforms gpt-4o), it should be discussed as a limitation.

- **The benchmark measures equilibrium computation from static payoff matrices, which is a narrower capability than the "strategic reasoning" framing suggests:** The paper defines strategic reasoning as "anticipating, planning, and responding to others' actions" (line 26). The core task — computing a pure-strategy Nash equilibrium from a fully specified payoff matrix — is a valid form of game-theoretic reasoning, but it does not involve interactive play, real-time adaptation, belief formation under uncertainty about opponents, or sequential opponent modeling (except in the complex forms, which are separate experiments). The complex forms partially address this, but the framing (Section 1) outstrips what the core benchmark measures. The paper should more carefully scope its claims.

### Trivial

- A few typographical issues: "the the difference" (line 159), "relately better" (line 230), "robuster" (line 238).

## Nice-to-Haves

- **Ablation study validating the need for exhaustive coverage:** The paper's core thesis is that limited game-type coverage produces unreliable evaluations. This could be demonstrated directly by computing model rankings using only the game types present in prior benchmarks and comparing them to the full 144-type ranking. If they diverge, that is direct evidence for the paper's motivation.

- **Discussion of why pure-strategy equilibria are the focus and mixed strategies are excluded:** The paper restricts to pure-strategy Nash equilibria without justification. Every finite game has at least one mixed-strategy equilibrium, and for 0-task games this is the only correct equilibrium concept. A brief justification or limitation statement would strengthen the paper.

- **Human baseline on the benchmark tasks:** Without a human accuracy anchor, claims about task difficulty are relative only to other models.

## Removed Points

These points were flagged by reviewers but removed after verification against the paper (with justification):

- **"0-task evaluation is underspecified / asymmetry finding may be an artifact":** The paper clearly specifies that 0-tasks have "no choice" as the standard answer (line 144) and that the standard heat map is "entirely blank" (line 275). The asymmetry finding is about the distribution of *wrong* answers (which quarter-grids models favor when they err), not about evaluation artifacts. A systematic non-random error pattern is precisely what makes the finding interesting. REMOVED — the criticism misreads what the asymmetry finding is.

- **"Bias Degree metric's symmetry assumption may not hold for TMGBench":** The paper explicitly states that the symmetry is a property of the Robinson-Goforth topology (line 162), not of TMGBench's specific implementation. There is no evidence that TMGBench violates this topological property. REMOVED — speculation without basis in the paper.

- **"No discussion of mixed-strategy equilibria / limitation of Robinson-Goforth topology":** The paper focuses on pure-strategy equilibria in 2×2 ordinal games, which is the scope of the Robinson-Goforth topology. Demanding coverage of mixed strategies or weak preferences is scope creep. REMOVED.

- **"No human baseline":** Generic request not specific to this paper's contribution. REMOVED.

- **"Nested form underspecified" / "infinite scalability unconvincing":** The nested form design is described (line 139), the paper demonstrates 2-fold nesting (line 282), and the claim about theoretical infinite scalability (line 141) is appropriately hedged as theoretical. REMOVED.

- **Generic formatting and reproducibility nitpicks** (e.g., undisclosed hyperparameters, missing appendix content). REMOVED per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the need for empirical comparison against GTBench as the highest-leverage improvement, and correctly identify that the sample-size limitations constrain the quantitative claims, but neither insight is novel beyond what the paper itself suggests or what is standard reviewer practice.

## Suggestions

1. Add an empirical comparison against GTBench (or other game-theoretic LLM benchmarks) showing either converging or diverging model rankings to validate the claim that exhaustive coverage matters.
2. Report confidence intervals or error bars for all quantitative claims, especially the 66.6%/60.0%/70.0% complex-form accuracies (20 runs each) and the coefficient-of-variation estimates (5 story-based instances).
3. Include the exact prompt templates and response-parsing logic in an appendix to fully specify the evaluation pipeline.
4. Acknowledge the GPT-4o-to-GPT-4o confound in the story-based generation pipeline as a limitation.
5. More carefully scope the claims: the core benchmark measures equilibrium computation from static payoff matrices, which is a facet of strategic reasoning but not the full definition given in the introduction.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>