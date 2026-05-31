## Human Reviewer 1

### Summary
Studies plasticity loss in deep RL under non-stationarity. The theory isolates two mechanisms: (i) NTK rank collapse across sequential warm-starts and (ii) a $\Theta (1/k)$ decay of the initial gradient each round. Motivated by (ii), the paper proposes Sample Weight Decay (SWD)—a lightweight recency-weighted replay scheme—to restore gradient magnitude. Experiments on TD3 (MuJoCo) and SAC with SimBa (DMC Humanoids/Dog) show consistent gains with reliable aggregate metrics (IQM/median/mean, bootstrap CIs) and a reverse ablation (SWA) that up-weights old samples and underperforms, alongside GraMa analyses.

### Strengths
- Identifies a crisp cause of plasticity loss and links it to a tractable remedy (recency weighting)
- Very simple algorithm (SWD) with negligible overhead, orthogonal to architectural methods (ReDo, Plasticity injection, etc.)
- Consistent empirical improvements across TD3 and SimBa-SAC; reverse ablation (SWA) plus GraMa trends support the mechanism.
- Uses reliable RL reporting (IQM/median/mean + stratified bootstrap CIs).

### Weaknesses
- Theory scope. Main results are derived for FQI-style/population losses; transfer to fully practical bootstrapped targets with representation drift is not fully established.
- Breadth. Evaluation is confined to continuous control; adding a pixel-based or sparse-reward task (e.g., DMControl pixels, AntMaze) would test generality.
- Over-edited text (LLM side-effects). While LLM assistance can improve flow/grammar, several sentences become awkward or semantically off and harm readability—for example, the abstract’s “How plasticity loss arises, dissipates and can be dissolved.” A careful human pass is needed to fix misuses and improve readability.
- Related work is too narrowly framed (over-emphasis on resets). The section concentrates on reset-style approaches while under-representing other relevant families—particularly **churn-reduction methods** and **auxiliary-loss–based representation stabilisation**. Please discuss these lines of work and clarify how SWD differs or complements them (see, e.g., churn-reduction: [https://arxiv.org/abs/2506.00592](https://arxiv.org/abs/2506.00592); auxiliary losses: [https://arxiv.org/abs/2405.00662](https://arxiv.org/abs/2405.00662)).

### Questions
- How sensitive are results to **linear vs. exponential** decay and to $((w_{\min}, T))$? Any failure modes with small buffers or rapid behaviour-policy shifts? 
- Do SWD’s benefits persist with **pixel observations** or **sparse rewards**? (A small add-on task would suffice.)

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper studies plasticity loss in deep RL through an optimization lens, identifying two mechanisms: (i) NTK rank degeneration and (ii) gradient attenuation that scales as Θ(1/k) under non-stationary data/targets with experience replay. Building on this analysis, the authors propose Sample Weight Decay (SWD)—a simple, plug-and-play, age-based sampling scheme for replay buffers that linearly down-weights older samples to counteract gradient decay and restore gradient magnitude. Experiments on MuJoCo (TD3) and DMC (SimBa-SAC) show consistent gains—including strong results on Humanoid—plus robustness across UTD ratios; ablations (including a reverse “SWA” variant) and GraMa measurements support the mechanism.

### Strengths
1. Clear theoretical framing with actionable takeaways. The paper formalizes how distribution/target non-stationarity yields NTK rank issues and a Θ(1/k) gradient-magnitude decay, then links performance to Bellman-residual control via a suboptimality bound—cleanly motivating data-weighting interventions.

2. Simple, general, and orthogonal method. SWD is an easy drop-in change to replay sampling, compatible with TD3/SAC (and, in principle, other replay-based methods) and positioned as orthogonal to architectural “plasticity-injection” tricks. The paper claims minimal overhead and plug-and-play practicality.

3. Compelling empirical evidence. Consistent improvements across MuJoCo and DMC (including Humanoid), robustness to varying UTD, and reverse validation via SWA plus GraMa analysis strengthen the causal story beyond raw scores.

### Weaknesses
1. Missing related work / plasticity literature coverage.

The related work should more deeply connect to recent plasticity and replay-weighting literature. Please discuss and contrast with, e.g.:

- Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning (ICML’24).
- Disentangling the causes of plasticity loss in neural networks (CoLLA’24).
- Hyperspherical Normalization for Scalable Deep RL (ICML’25).
- Mitigating Plasticity Loss in Continual RL by Reducing Churn (ICML’25).
- A Forget-and-Grow Strategy for Deep RL Scaling in Continuous Control (ICML’25).

2. Overlapping idea; contribution clarity vs ER-decay.

Conceptually, SWD (linear, age-based down-weighting) looks very close to prior ER-decay heuristics, with differences seemingly in coefficients/schedules. The paper does offer more formalism, but the delta in contribution should be crystal clear: which parts are novel theory, which are new algorithmic prescriptions beyond a tuned decay, and what guarantees (if any) distinguish SWD from ER-decay? I’m open to a high score even if the mechanism is similar—provided the theoretical backup and empirical analysis are meticulous and make the case for why this instantiation is principled/non-equivalent.

3. Implementation and efficiency details are thin.

A per-sample weight update naively done every step can be costly. Please:
- Describe the efficient implementation (lazy updates? piecewise-linear buckets? periodic renormalization?).
- Report end-to-end wall-clock and GPU-hour costs on standard hardware for SimBa vs SimBa+SWD;

### Questions
1. Beyond sample-efficient regimes. 

Authors primarily test in sample-efficient settings. What happens with very long training (e.g., 10M env steps with a 1M buffer) where fresh samples repeatedly overwrite older ones? Do you observe more catastrophic forgetting under high churn, and does SWD still mitigate it or saturate? (This is important because small buffers + long horizons can exacerbate plasticity.)



I’m open to increasing the score if the authors adequately address the weaknesses—particularly by deepening related work discussion, clarifying the novelty relative to ER-decay, and detailing the efficiency and long-horizon robustness experiments.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper investigates plasticity loss in deep reinforcement learning from a theoretical optimization perspective. The authors identify two mechanisms causing plasticity loss: (1) rank collapse of the Neural Tangent Kernel (NTK) Gram matrix, and (2) Θ(1/k) decay of gradient magnitude during training. Based on this analysis, they propose Sample Weight Decay (SWD), a lightweight sampling strategy that assigns higher probabilities to more recent samples in the replay buffer to counteract gradient attenuation. Experiments on MuJoCo and DeepMind Control Suite tasks with TD3 and SAC algorithms demonstrate consistent performance improvements.

### Strengths
- SWD is remarkably simple to implement with minimal computational overhead, making it easily applicable across different RL algorithms and architectures as a plug-and-play solution, which is practically valuable compared to more invasive methods.
- The experimental validation is comprehensive, including evaluation on two benchmark suites, comparison with PER, reverse validation through SWA ablation, plasticity measurement using GraMa metrics, and robustness analysis across different UTD ratios, all showing consistent improvements.

### Weaknesses
1. The linear decay design of SWD (w_i = max(w_min, 1 - age_i/T)) appears somewhat arbitrary without clear theoretical justification for why this particular weighting scheme optimally compensates for the 1/k gradient attenuation. Sensitivity analysis on decay schedules and hyperparameters is insufficient.

2. Recency-based sampling is not novel conceptually, and the paper lacks direct comparisons with recent plasticity-preserving methods (ReDo, ReGraMa, Plasticity Injection). The claimed "SOTA performance" is primarily against uniform sampling and PER, making it difficult to assess the true contribution relative to the current state of the art.

### Questions
1. Can you provide rigorous analysis showing how the gradient dynamics derived for FQI extend to deep RL algorithms with experience replay and bootstrapping? How does the 1/k decay manifest in TD3/SAC specifically?
2. How sensitive is SWD to hyperparameters T and w_min? Tables 5-6 show different T values—how were these chosen? Have you systematically compared different decay schedules (exponential, polynomial, etc.)?
3. Since you claim SWD is orthogonal to existing methods, have you tested combinations with network reset or neuron recycling? Can you provide direct experimental comparisons with ReDo, ReGraMa, and Plasticity Injection to substantiate the SOTA claim?

I will consider increasing the score if the author responds to these questions.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper studies plasticity loss in deep RL and attributes it to two mechanisms induced by non-stationarity: (i) NTK Gram rank collapse, and (ii) attenuation of gradient magnitudes that decays as $\Theta(1/k)$ over training iterations $k$. Motivated by the second mechanism, the authors propose Sample Weight Decay (SWD): linearly down-weight older transitions in the replay buffer so that recent data counteracts the $\Theta(1/k)$ decay and restores effective gradient scale. SWD is plug-and-play for replay-based algorithms.  
Empirically, SWD is added to TD3 and SimBa-SAC on MuJoCo and DMC tasks, with strong gains on DMC Humanoid. A “reverse” ablation (SWA, which up-weights old data) predictably reduces gradient norms and hurts returns, supporting the causal story.

### Strengths
1. Tight theory to method link: The $\Theta(1/k)$ gradient attenuation analysis (Theorem 3) cleanly motivates SWD’s linearly decaying replay weights; the SWA “reverse” ablation strengthens causal plausibility.  
2. Simple and orthogonal: SWD lives at the sampling layer, is easy to add to any replay-based RL algorithm, and should compose with model-level plasticity fixes.  
3. Compelling results on hard control: Consistent improvements, with standout gains on DMC Humanoid, suggest the effect is meaningful, not a small-n artifact.

### Weaknesses
1. Unprobed NTK mechanism: The paper posits NTK rank collapse but provides no spectrum or conditioning measurements; half of the causal story remains speculative.  
2. Missing SOTA positioning: No head-to-head (or composition) with recent plasticity remedies such as ReGraMa, Plasticity Injection, or ReDo, leaving SWD’s incremental or additive value unclear.  
3. Practical knobs under-explored: No sensitivity for $T$ (linear decay steps) and $w_{\min}$; interactions with PER are not clarified (do they stack or conflict?); runtime or throughput impact is unreported.

### Questions
1. NTK evidence: Can you track NTK Gram eigenvalues (or condition number) on fixed probe batches across training, ideally under “sequential initialization,” to confirm or quantify rank collapse?  
2. Comparisons or compositions: How does SWD compare to and combine with ReGraMa or Plasticity Injection on a small DMC subset (including an SWD+X variant) to establish additivity?  
3. Sensitivity and heuristics: Please add curves for $T$ and $w_{\min}$. Is a simple heuristic (for example, $T$ as a fraction of buffer capacity or tied to a gradient-norm half-life) a reasonable default for new domains?

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
6

### Confidence
3