

{0}------------------------------------------------

# Geometric Flow Networks: A Physics-Informed Paradigm for Sequential Intelligence

Joaquín Stürtz  
DepthMuun Research

April 15, 2026

## Abstract

**Geometric Flow Networks (GFN)** constitute a paradigm of neural computation that formalizes intelligence as the continuous evolution of a persistent internal world governed by structural invariants. Unlike the stateless correlation computed by self-attention mechanisms, GFN treats computation as the trajectory of a state vector flowing through a geometric manifold where inputs act as external perturbations that curve the trajectory without replacing the state. This architecture ensures that information is transformed according to structural conservation laws rather than being transiently buffered or destroyed, thereby enabling a **demonstrated** constant-memory footprint for the **Recursive State Memory** regardless of context length.

Two distinct realizations demonstrate the paradigm’s scope and generality. The Geodesic State Space Model (G-SSM) formalizes representation as a continuous flow on a learned Riemannian manifold, evolving phase-space variables  $(\mathbf{x}, \mathbf{v})$  through symplectic integration. In parallel, the Inertial State Network (ISN) implements a deep stateful pipeline where both semantic scanning and world evolution maintain persistent momentum. Our empirical evaluations establish a rigorous efficiency benchmark on entry-level hardware (GTX 1650): the ISN achieves character-level language generation with a perplexity of **2.48** using only **363,329 parameters**. In long-context inference ( $L = 2000$ ), the ISN maintains a throughput of **700 TPS**, significantly outperforming Transformer baselines which exhibit  $O(N^2)$  degradation. Under optimized environments (HuggingFace Spaces), the system demonstrates a peak performance of up to **2,000 TPS**, highlighting the inherent scalability of the geodesic flow engine.

By shifting from statistical correlation to structure-preserving dynamics, GFN enables a theoretical constant state memory complexity and significant parameter reduction. While the paradigm provides **structural grounding** against hallucinations through deterministic invariants, we observe that in open-domain generative tasks, the effectiveness of this resistance is coupled to the scale and precision of the learned manifold metrics. Our findings indicate that while topological constraints offer absolute guarantees in logic, linguistic domains exhibit a “soft” resistance subject to metric resolution.

**Cite as:** Stürtz, J. (2026). Geometric Flow Networks: A Paradigm for Sequential Intelligence. *GFN Research Preprint*. DOI: 10.5281/zenodo.19141132

{1}------------------------------------------------

Code and models are available at <https://github.com/DepthMuun/gfn> and <https://huggingface.co/DepthMuun>.

## 1 Introduction

The deep learning revolution of the past decade has been fundamentally defined by a single architectural choice: the attention mechanism. Introduced by Vaswani et al. [19], self-attention enabled unprecedented parallelization in sequence modeling. Consequently, it scaled to become the technical backbone of modern large language models, vision transformers, and multimodal architectures.

The phrase “Attention Is All You Need” proved to be a foundational insight [19]; the architecture now serves as the primary basis upon which contemporary large-scale sequence modeling rests. However, we argue that this success represents a local maximum within the statistical paradigm. The attention mechanism treats reasoning as correlation maximization throughout a sequence. We propose **Geometric Flow Networks (GFN)** as a structural alternative that shifts the computational burden from statistical sampling to geodesic integration.

As a structural paradigm, GFN shifts the computational focus from statistical correlation to state-persistent physical evolution. In this work, we present two distinct architectures that instantiate this paradigm:

1. **Geodesic State Space Model (G-SSM)**: A differential realization that formalizes the framework as a second-order manifold state space model, evolving continuous phase-space variables through symplectic integration of learned curvature.
2. **Inertial State Network (ISN)**: A continuous dynamic system that implements the same physical principles through geometric state persistence, where information is lived by a particle flowing through manifold curvature rather than stored in memory buffers.

### 1.1 The Statistical Foundation and Its Limitations

The attention mechanism computes a weighted sum over all positions in a sequence:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V \quad (1)$$

where queries  $Q$ , keys  $K$ , and values  $V$  are linear projections of input representations. The softmax operation converts dot-product similarities into a probability distribution, effectively treating all token relationships as potentially significant until proven otherwise. This design choice carries several fundamental consequences:

- **Quadratic Memory:** The  $O(N^2)$  memory scaling of attention with respect to sequence length creates barriers that constrain practical context lengths and necessitates expensive memory management strategies like KV-caches.
- **Stateless Computation:** Each forward pass treats tokens as independent observations to be correlated rather than as states in a dynamical system. This statelessness mandates explicit memory storage through KV-caches rather than implicit state compression.
- **Probabilistic Hallucination:** Because attention operates on learned correlations without grounding in physical constraints, models frequently produce outputs that

{2}------------------------------------------------

are statistically plausible but semantically invalid. These hallucinations emerge from the system’s inability to distinguish between correlation and causality.

### 1.2 The Path Forward: Physics-Based Intelligence

We propose that the next paradigm shift requires abandoning the statistical foundation in favor of a physics-informed approach. Rather than merely learning token correlations, we propose learning the **structural invariants** of the domain: the fundamental laws governing valid state transitions. Within this framework, we introduce **Geometric Flow Networks (GFN)**, a paradigm in which computation is formalized as a particle flowing through a structured state space. This transition offers several theoretical advantages:

- **Recursive State Persistence:** Once the domain’s invariants are captured, information is preserved through state persistence rather than explicit history buffering. The internal world model (the latent state) operates as a persistent geometric configuration, dramatically reducing the memory overhead associated with context expansion through its intrinsic nature rather than explicit caching.
- **Architectural Agnosticism:** If the model learns the underlying physics of a domain, different signals (text, image, audio) represent distinct projections of the same invariant structure, enabling native multimodality through geometric unification.
- **Deterministic Grounding:** Physical constraints enforce validity conditions that provide a structural resistance to hallucination, moving from statistical regularizers to hard-coded geometric boundaries.

By replacing probability with structured state evolution, the **GFN Paradigm** escapes the boundaries of quadratic memory scaling and statistical hallucination. The following sections formalize this framework and demonstrate its empirical efficacy across both differential and continuous dynamic domains, establishing a deterministically stable foundation for the next generation of artificial intelligence.

## 2 Theoretical Foundations

### 2.1 The Geometric Locus of Intelligence

We begin by formalizing the distinction between statistical attention and geometric interaction. In the Transformer paradigm, an input sequence  $\mathbf{x} = (x_1, \dots, x_N)$  exists in a flat embedding space where relevance is a measure of learned similarity. In this framework, reasoning reduces to computing weighted averages based on dot-product similarities.

In contrast, our framework treats inputs as forces that perturb a geometric entity flowing through a structured **geometric locus**  $\mathcal{M}$  (the domain of validity). Each valid cognitive state or relationship corresponds to a point within this structured domain, and reasoning is defined as the **structural evolution** of state following geodesic trajectories through the manifold. Crucially, the GFN paradigm is agnostic to the specific mathematical formalism of  $\mathcal{M}$ : it may be instantiated as a Riemannian manifold with Christoffel symbols, a discrete transition graph obeying conservation laws, or a continuous flow field, provided the evolution satisfies the five defining pillars of the paradigm.

The fundamental equation governing this flow (Equation 2) is:

$$\mathbf{y} = \gamma_{\mathcal{M}}(0, 1; \mathbf{x}_0, \mathbf{v}_0) \tag{2}$$

{3}------------------------------------------------

where  $\gamma_{\mathcal{M}}$  represents the geodesic trajectory on manifold  $\mathcal{M}$  starting from initial position  $\mathbf{x}_0$  with initial velocity  $\mathbf{v}_0$ , arriving at final state  $\mathbf{y}$ . The state does not teleport between configurations; it flows continuously through the geometry.

### 2.2 The Structural Evolution Principle

The GFN paradigm defines intelligence as the evolution of a state  $(\mathbf{x}, \mathbf{v})$  according to a **stationary action principle**. In this view, a sequence of inputs acts as a series of perturbations (forces) that bend the geodesic trajectory of the particle through the manifold. The trajectory is governed by a generalized flow operator  $\mathcal{F}$  (Equation 3):

$$\frac{d\mathbf{x}}{dt} = \mathbf{v}, \quad \frac{d\mathbf{v}}{dt} = \mathcal{F}(\mathbf{x}, \mathbf{v}, \mathbf{f}_{ext}; \theta) \quad (3)$$

where  $\mathcal{F}$  is designed to preserve specific **structural invariants** of the domain while accepting external force perturbations  $\mathbf{f}_{ext}$ .

In the differential realization (**G-SSM**), this evolution is formalized as a **geodesic flow** on a learned Riemannian manifold  $\mathcal{M}$ . The trajectory follows the geodesic equation:

$$\frac{d^2x^i}{dt^2} + \Gamma_{jk}^i \frac{dx^j}{dt} \frac{dx^k}{dt} = 0 \quad (4)$$

where  $\Gamma_{jk}^i$  (Christoffel symbols) represent the learned curvature of the semantic space. Logical consistency corresponds to following the path of least resistance through continuous phase space.

Conversely, in the continuous dynamic realization (**ISN**), the evolution  $\mathcal{F}$  is instantiated through **continuous geodesic flow** where the state's momentum carries it forward even when no external forces are applied. The key distinction from G-SSM is that ISN eliminates discrete timesteps entirely, treating state evolution as a continuous differential flow governed by three principles:<sup>1</sup> (1) **State Inertia**: the world persists without external clock synchronization; (2) **Geometric Coupling**: inputs curve the trajectory without replacing state; (3) **Manifold Omnipresence**: all computation occurs within invariant-preserving geometry.

### 2.3 Conservation Laws and Noether's Theorem

The stability of trajectories on  $\mathcal{M}$  is guaranteed by embedding conservation laws directly into the architecture. In physical systems, conserved quantities (mass, energy, momentum) constrain possible evolutions. According to Noether's Theorem [14], every differentiable symmetry of a physical system's action corresponds to a conservation law.

By designing the manifold  $\mathcal{M}$  to possess specific geometric symmetries, we ensure that the corresponding conservation laws are hard-coded into the model's dynamics. For example, in the domain of integer parity (XOR), the parity of the world state must be conserved across operations. This stands in contrast to statistical attention, where constraints are limited to soft probabilistic normalization. In a geometric framework,

---

<sup>1</sup>This represents a fundamental departure from discrete recursions ( $h_{t+1} = f(h_t, x_t)$ ) to continuous vector fields ( $\frac{d\mathbf{x}}{dt} = f(\mathbf{x}, u(t))$ ), enabling temporal resolution independence where the state can be queried at arbitrary time points (e.g.,  $t = 1.5, t = 1.0001$ ); this constitutes a theoretical capability of the continuous GFN paradigm beyond discrete token-based implementations.

{4}------------------------------------------------

violations are not merely unlikely: they are geometrically inconsistent with the chosen topology, making them structurally impossible rather than statistically improbable:

$$\sum_i \psi_k(\text{input}_i) = \text{State}_k(\text{world}) \quad (5)$$

where  $\psi_k$  represents a conserved property mapping and the equality is enforced by the geometry rather than learned through statistics.

## 3 The Five Pillars of Geometric Flow Networks

The **Geometric Flow Networks (GFN)** paradigm is defined by five structural pillars that capture its philosophical essence rather than prescribing specific implementations. These pillars distinguish GFN from both statistical models (attention, SSMs) and generic continuous models (Neural ODEs) by articulating what the paradigm fundamentally *\*is\**, not how it must be *\*computed\**:

1. **Geodesic State Flow:** The state evolves as a continuous trajectory through a learned geometry, not as a statistical transformation of tokens. This pillar captures the essential nature of GFN computation: the system computes transitions as flow along geodesics in a manifold where valid transitions correspond to trajectories of minimal resistance. Unlike attention which computes weighted correlations, GFN computes how state moves through semantic curvature. The state possesses “semantic inertia”: history manifests as trajectory shape, not as explicit storage.
2. **Persistent Internal World:** The state exists as a geometric configuration that persists independently of inputs; inputs perturb the trajectory without replacing the state. This pillar articulates an ontological distinction: the internal world is not a memory buffer that stores history (like a KV-cache), but a reality that *\*is\**. Inputs do not add information to a list; they curve the space-time where the state orbits. A Transformer without KV-cache forgets everything; the GFN world exists as geometry itself, not as a record of events.
3. **Structural Invariance:** At least one conservation law (physical, logical, or topological) governs valid transitions, making certain states structurally impossible rather than merely improbable. This is the paradigm’s most philosophically distinctive pillar. Invariants are not soft regularization or probabilistic normalization (like softmax in attention), but physical laws encoded in geometry. In logical domains (XOR), the space has toroidal topology: invalid transitions are geometrically impossible. In semantic domains, invariants are “soft” but remain structural, not statistical.
4. **Causal Locality:** Dynamics emerge from local interactions (forces, curvature, couplings), not from global correlation over the entire sequence. This pillar distinguishes GFN from architectures requiring simultaneous access to all historical context. Locality here is not necessarily spatial (as in CNNs) but causal: the next state depends on forces acting on the current state, not on computing similarity with all prior tokens. This enables memory without memory buffers.
5. **Physics-Grounded Computation:** Validity constraints are geometric and topological, not statistical; coherence is measured in terms of curvature and conservation, not likelihood. This pillar articulates that GFN is not “more of the same with a different name”. Constraints are not learned statistics or probabilistic normalization,

{5}------------------------------------------------

but validity conditions encoded in geometry. The system “knows” which states are invalid because they are topologically inconsistent, not because they are statistically improbable.

Two architectures demonstrate the paradigm’s scope: G-SSM operates in continuous phase space with explicit symplectic integration, while ISN operates as a continuous dynamic system with implicit geodesic flow. Both satisfy all five pillars by capturing their philosophical essence rather than adhering to specific algorithmic constraints.

### 3.1 Realization A: Geodesic State Space Model (G-SSM)

The **G-SSM** is the discrete-integration realization of the GFN paradigm. It satisfies the five pillars through the following mechanisms:

- **Adaptive Riemannian Metrics:** Dynamic estimation of the domain’s metric tensor, allowing the model to non-linearly transform its tangent space to match the logical requirements of the token sequence.
- **Stability Sidecars:** Specific implementations of G-SSM incorporate *Singularity Gating* and *Numerical Hysteresis* to manage finite-precision effects, along with *Holographic Dynamics* for associative state persistence.

The G-SSM treats each input token as an external force that perturbs the geodesic flow. The state’s trajectory is determined by the competition between its inherited momentum and the curved geometry of the manifold, with external inputs bending but not replacing the configuration.

### 3.2 Realization B: Inertial State Network (ISN)

The **ISN** represents a continuous dynamic realization of the GFN paradigm that satisfies all five pillars through its unique architectural design. Unlike G-SSM, which operates through discrete symplectic integration steps, the ISN eliminates fixed timesteps entirely, treating state evolution as a continuous differential flow governed by geodesic inertia. In this framework, information is not stored but lived: state flows through manifold curvature, and the past shapes the future not through accumulation but through the way history has molded the trajectory.

The ISN is architecturally defined by three core modules that implement the five GFN pillars:

1. **GFNScanner:** An embedding layer followed by flow dynamics via  $\tanh(W \cdot s)$ , where  $s$  is the current state. This module encodes tokens as impulses and maintains persistent semantic momentum.
2. **GFNWorld:** The core state evolution engine implementing geodesic flow through drift (inertia) and diffusion (external impulses). The update rule is:

$$\mathbf{W}_{t+1} = \mathbf{W}_t + \text{drift}(\mathbf{W}_t) + \text{diffusion}(\mathbf{f}_{\text{ext}}) \quad (6)$$

where  $\mathbf{W}_t$  is the persistent world state, ensuring  $O(1)$  memory complexity through state persistence rather than history accumulation.

3. **ThresholdEmitter:** The materialization layer that projects world states to token logits through learned thresholds, completing the pipeline from geometric state to discrete output.

{6}------------------------------------------------

![Diagram of the High-Fidelity G-SSM Architecture. The flow starts with State: [x, v]_t entering the Γ-Predictor (Metric Core). Tokens f_{xt} are also input to the Γ-Predictor and the Force Accumulator Σ φ. The Γ-Predictor outputs to the Force Accumulator. The Force Accumulator outputs to the Symplectic Integrator (Leapfrog). The Symplectic Integrator outputs to the Neural Refinement (Mixer/Dynamics). The Neural Refinement outputs to the Topology Projection / Normalization. The Topology Projection / Normalization outputs to State: [x, v]_{t+1}. A dashed blue arrow labeled 'State Persistence Loop (Geodesic Flow)' connects the final state back to the initial state. Three optional sidcar modules (dashed boxes) are shown: Hysteresis (Memory) with 'Stability/Memory Sidcar' label, Singularity Shield, and Adaptive Δt, all connected to the Force Accumulator and Symplectic Integrator.](fc46871d72c65d3381d9201646d23439_img.jpg)

Diagram of the High-Fidelity G-SSM Architecture. The flow starts with State: [x, v]\_t entering the Γ-Predictor (Metric Core). Tokens f\_{xt} are also input to the Γ-Predictor and the Force Accumulator Σ φ. The Γ-Predictor outputs to the Force Accumulator. The Force Accumulator outputs to the Symplectic Integrator (Leapfrog). The Symplectic Integrator outputs to the Neural Refinement (Mixer/Dynamics). The Neural Refinement outputs to the Topology Projection / Normalization. The Topology Projection / Normalization outputs to State: [x, v]\_{t+1}. A dashed blue arrow labeled 'State Persistence Loop (Geodesic Flow)' connects the final state back to the initial state. Three optional sidcar modules (dashed boxes) are shown: Hysteresis (Memory) with 'Stability/Memory Sidcar' label, Singularity Shield, and Adaptive Δt, all connected to the Force Accumulator and Symplectic Integrator.

**Figure 1: High-Fidelity G-SSM Architecture:** The semantic state is propagated through a symplectic geometric engine, refined by a neural dynamics filter, and projected onto the manifold topology. The "Persistence Loop" ensures that token-induced forces update continuous phase-space variables (position and momentum) rather than transient embeddings. The optional **sidcar modules** (dashed box) are experimental components for stability research; the system is capable of learning the underlying domain physics natively via the core geodesic engine.

In the current autoregressive realization, the ISN flows through geometry at discrete intervals dictated by high-frequency sampling (the tokenizer), though the internal dynamics admit arbitrary temporal resolution. The detailed internal architecture is illustrated in Figure 2.

By prioritizing continuous geodesic flow over discrete token processing, the **ISN** achieves what we term Inertia-Grounded Intelligence: a form of computation where reasoning emerges from the geometry of a persistent internal world rather than from statistical associations between discrete tokens.

## 4 The Computational Advantage

### 4.1 Complexity Analysis: $O(1)$ vs. $O(N^2)$

The computational complexity distinction between attention and geometric interaction has profound practical implications for memory scaling and inference efficiency.

**Notes:** The **ISN** forward pass is  $O(N)$  in terms of total sequential latency, reflecting the inherent causality of generation. However, the **per-token step complexity** is strictly  $O(1)$  with respect to context length, as the model avoids the quadratic re-processing of history through its persistent state. We distinguish between the **Recursive State**

{7}------------------------------------------------

![Diagram of the ISN Architecture showing the flow from Input Tokens to Output Tokens through GFNScanner, GFNWorld, and ThresholdEmitter components.](3121ebddccf183ca63bb9781be440a7e_img.jpg)

```

graph TD
    Input[Input Tokens  $S_{1..N}$ ] --> GFNScanner[GFNScanner]
    subgraph GFNScanner
        E[Embedding Layer]
        F[Flow Dynamics  $\tanh(W \cdot s)$ ]
    end
    GFNScanner --> GFNWorld[GFNWorld]
    subgraph GFNWorld
        D[Drift (Inertia)]
        Diff[Diffusion  $(\Phi_{wt})$ ]
        LN[LayerNorm]
    end
    SP[State Persistence  $W_t$ ] -.-> GFNWorld
    GFNWorld --> TE[ThresholdEmitter]
    TE --> Output[Output Tokens  $Y$ ]
  
```

Diagram of the ISN Architecture showing the flow from Input Tokens to Output Tokens through GFNScanner, GFNWorld, and ThresholdEmitter components.

**Figure 2: ISN Architecture:** The ISN implements three core components: (1) **GFNScanner** embeds tokens and applies flow dynamics via  $\tanh(W \cdot s)$ ; (2) **GFNWorld** evolves the persistent state  $\mathbf{W}$  through drift (inertia) and diffusion (external impulses) with  $\mathbf{W}_{t+1} = \mathbf{W}_t + \text{drift}(\mathbf{W}_t) + \text{diffusion}(\mathbf{f}_{ext})$ ; (3) **ThresholdEmitter** materializes world states to logits. The state persistence loop ensures  $O(1)$  memory complexity. Unlike G-SSM which uses symplectic integration, ISN employs continuous differential flow where momentum carries state forward without discrete timesteps at the dynamical level.

**Memory** ( $O(1)$ ), which represents the core persistent world model, and the **Processing Buffer** ( $O(N)$ ) used in current batch implementations for gradient accumulation and monitoring. The key insight is that once the structural invariants are learned, updating the trajectory requires only the current state configuration. We distinguish between **State Memory Persistence** ( $O(1)$ ), and the **Emission Buffer** ( $O(N)$ ), which gathers generated tokens for external decoding.

**Table 1:** Complexity comparison between attention mechanism and geometric interaction.

| Metric | Attention | ISN (GFN) |
|-|-|-|
| Batch Forward ( $N$ tokens) | $O(N^2 \cdot d)$ | $O(N \cdot d)$ |
| Step Complexity (per token) | $O(N \cdot d)$ | $O(1)$ |
| Inference Memory | $O(N \cdot d)$ | $O(1)$ |
| Inference Speed ( $L = 2000$ , GTX 1650) | 231 TPS | <b>700 TPS</b> |
| Training Memory | $O(N \cdot d)$ | $O(1)^\dagger$ |

<sup>†</sup>The GFN paradigm achieves  $O(1)$  through the Adjoint Sensitivity Method. Current modular implementations exhibit  $O(N)$  scaling due to gradient accumulation in standard backpropagation, though with several orders of magnitude lower constants than attention.

{8}------------------------------------------------

Furthermore, G-SSM avoids the  $O(d^3)$  complexity of brute-force Christoffel computation by utilizing a **Low-Rank Riemannian Decomposition**:

$$\Gamma_{ij}^k \approx \sum_{r=1}^R W_{rk}(U_{ir}U_{jr}) \quad (7)$$

where  $R \ll d$ . This reduces the contraction cost to  $O(d^2R)$ , making the system scalable to high dimensions ( $d > 512$ ) comparable to Transformer blocks, while naturally regularizing the metric manifold through the low-rank constraint to ensure positive-definite stability.

Furthermore, unlike standard backpropagation through time (BPTT), which requires storing all intermediate activations ( $O(N)$  memory), geometric models can utilize the **Adjoint Sensitivity Method** [3, 15]. Formally, the method computes the gradient of a loss  $\mathcal{L}$  with respect to the state  $\mathbf{x}(t)$  by solving an adjoint differential equation backwards in time:

$$\frac{d\mathbf{a}}{dt} = -\mathbf{a}(t)^\tau \frac{\partial \mathcal{F}}{\partial \mathbf{x}} \quad (8)$$

where  $\mathbf{a}(t) = \partial \mathcal{L} / \partial \mathbf{x}(t)$  is the adjoint state. This allows computing gradients by solving a second, adjoint ODE backwards in time, reducing training memory complexity to  $O(1)$  with respect to sequence length. This makes **G-SSM** uniquely suitable for training on massive contexts (e.g., 1, 000, 000+ tokens) that would be physically impossible for attention-based architectures to fit in VRAM. Regarding sequential latency, GFN accepts  $O(N)$  temporal processing as a fundamental tradeoff for long-horizon persistence, prioritizing structural integrity over the burst-parallelization of stateless models.

### 4.2 Architectural Modality-Agnosticism Through Geometric Unification

A notable advantage of the geometric approach is **modality-agnosticism**: the ability to support heterogeneous inputs without core architectural modification. Different modalities appear as distinct projections of the same underlying structural reality.

An image of a cat and the text “cat” both correspond to the same concept in the semantic manifold. Statistical models must learn this correspondence through joint training on paired data: a soft association that can fail when faced with novel combinations. Geometric models can represent the concept as a single point on the manifold, with different modalities providing different coordinate representations of the same geometric entity:

$$\text{Cat}_{\text{image}} = \text{Proj}_{\text{image}}(\mathbf{p}) \quad (9)$$

$$\text{Cat}_{\text{text}} = \text{Proj}_{\text{text}}(\mathbf{p}) \quad (10)$$

$$\text{Cat}_{\text{audio}} = \text{Proj}_{\text{audio}}(\mathbf{p}) \quad (11)$$

where  $\mathbf{p}$  is the invariant geometric representation and  $\text{Proj}$  represents the modality-specific projection. The GFN paradigm proposes that what is shared across modalities is not merely a static point in space, but the **dynamical invariants** (the physics engine) that govern how those points evolve. Once the underlying transition laws are established, modality transitions become equivariant transformations rather than complex mapping problems.

### 4.3 Out-of-Distribution Generalization

Statistical models generalize through interpolation in high-dimensional embedding space. This generalization is inherently limited by the training distribution: any input outside this distribution requires extrapolation, which statistical models perform poorly.

{9}------------------------------------------------

Geometric models generalize through extrapolation along learned manifolds. The key distinction is philosophical rather than merely technical. A statistical model asks “what have I seen before?” A geometric model asks “what is physically possible given the invariants that govern this domain?” When asked about symbolic logic or sequence patterns not seen in training:

- A statistical model outputs the most probable continuation based on observed patterns, which may fail when patterns deviate from training distribution.
- A geometric model computes the unique result consistent with the conservation laws defining the manifold, which must hold regardless of training distribution.

This distinction is fundamental. Statistical models can only reproduce patterns; geometric models can compute novel combinations because they understand the underlying structure governing valid states. The particle flows along geodesics determined by geometry, and these geodesics exist independently of what combinations were observed during training.

## 5 The Free Energy Principle and Computational Neuroscience

### 5.1 Connection to Friston’s Free Energy Principle

Our framework resonates strongly with Karl Friston’s Free Energy Principle [7], which proposes that all biological systems minimize free energy to maintain homeostasis. Under this framework, perception is inference about hidden states of the world, and action serves to minimize surprise (the difference between predicted and observed sensory inputs).

We argue that geometric interaction directly implements free energy minimization:

1. **Prediction:** The geometric manifold defines possible states; predictions correspond to the most likely point on this manifold given current momentum and position.
2. **Inference:** Observing new data constrains the feasible region on the manifold through force perturbations; inference narrows to states consistent with both prior geometry and new observations.
3. **Action:** Interventions test predictions; the system updates its geodesic trajectory to minimize discrepancy between predicted and observed states.

The attention mechanism, by contrast, treats prediction as pattern matching: a fundamentally different computational strategy that lacks the geometric grounding necessary for structural inference. Geometric models implement active inference through continuous flow; statistical models implement passive pattern completion through weighted averaging.

### 5.2 Implications for Neuromorphic Computing

The computational structure of geometric interaction aligns naturally with physical computing substrates. This alignment suggests future hardware directions that we believe will prove more efficient for geometric models:

- Attention requires random access to arbitrary memory locations (the KV-cache) and dense matrix multiplication: operations well-suited to digital computers but poorly suited to analog or neuromorphic systems.

 Rest of paper (reference and Appendix) is removed.