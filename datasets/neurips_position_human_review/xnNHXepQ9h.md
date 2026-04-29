# Position: AI Should Sense Better, Not Just Scale Bigger: Adaptive Sensing as a Paradigm Shift

- Decision: Accept
- Scores: 7, 5, 4

## Abstract
Current AI advances largely rely on scaling neural models and expanding training datasets to achieve generalization and robustness. Despite notable successes, this paradigm incurs significant environmental, economic, and ethical costs, limiting sustainability and equitable access. Inspired by biological sensory systems, where adaptation occurs dynamically at the input (e.g., adjusting pupil size, refocusing vision)—we advocate for adaptive sensing as a necessary and foundational shift. Adaptive sensing proactively modulates sensor parameters (e.g., exposure, sensitivity, multimodal configurations) at the input level, significantly mitigating covariate shifts and improving efficiency. Empirical evidence from recent studies demonstrates that adaptive sensing enables small models (e.g., EfficientNet-B0) to surpass substantially larger models (e.g., OpenCLIP-H) trained with significantly more data and compute. We (i) outline a roadmap for broadly integrating adaptive sensing into real-world applications spanning humanoid, healthcare, autonomous systems, agriculture, and environmental monitoring, (ii) critically assess technical and ethical integration challenges, and (iii) propose targeted research directions, such as standardized benchmarks, real-time adaptive algorithms, multimodal integration, and privacy-preserving methods. Collectively, these efforts aim to transition the AI community toward sustainable, robust, and equitable artificial intelligence systems.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This paper champions the idea of "adaptive sensing" as a groundbreaking shift in how we develop AI, steering away from the usual focus on just scaling up neural models and datasets. Taking cues from how biological sensory systems work, the authors suggest that AI should focus on dynamically fine-tuning sensor parameters - like exposure, sensitivity, and multimodal setups - right at the input stage, instead of just relying on bigger models. They provide compelling evidence that adaptive sensing can help smaller models outperform much larger ones while also cutting down on computational costs. The paper introduces a closed-loop framework for embodied AI agents and lays out research paths for weaving adaptive sensing into various fields such as robotics, healthcare, and autonomous systems. The key takeaway is that this approach paves the way for a more sustainable, efficient, and fair AI landscape.

### Strengths
The paper presents an engaging vision for sustainable AI through adaptive sensing, supported by some promising initial evidence. The biological inspiration is not only well-justified but also clearly articulated. It offers a thorough roadmap that covers various application areas, complete with tangible examples. The writing style is approachable, making it easy for readers without deep technical knowledge to grasp the concepts. This topic tackles pressing issues regarding the environmental and societal effects of AI. Additionally, the proposed framework effectively connects different research fields. The formal mathematical foundation for embodied AI provides a solid technical basis.

### Weaknesses
The evidence we have mainly comes from image classification tasks, and it shows some limitations in generalization. This paper is quite lengthy for a position paper, which might make it less accessible to some readers. Some of the claims regarding the potential of adaptive sensing could be a bit exaggerated, especially considering the limited evidence available. The section on challenges could do a better job of addressing the fundamental limitations we face. Additionally, alternative methods for sustainable AI, like efficient architectures and federated learning, don’t get much attention. It seems like the complexity of putting adaptive sensing into practice in real-world systems might be underestimated. A more detailed analysis of when adaptive sensing is truly beneficial would really bolster the argument.

### Questions
How does the computational overhead of continuously adapting sensors stack up against the claimed efficiency gains, especially in environments with limited resources? 

What specific benchmarks or evaluation frameworks could effectively showcase the advantages of adaptive sensing across various tasks, beyond just image classification? 

How would adaptive sensing hold up in situations where the best sensor configurations are highly dependent on the task at hand or change quickly?

### Presentation
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper argues for adaptive sensing as a fundamental paradigm shift away from the model-centric adaptation and generalization in the current mainstream AI communities. The authors draw inspiration from biological sensory systems that dynamically adjust parameters, such as pupil size and focus. The central claim in the paper is that current foundation models' reliance on scaling compute and datasets creates unsustainable environmental, economic, and ethical costs while failing to address real-world domain shifts efficiently and effectively.
The authors mainly support their position through evidence from existing computer vision domains, theoretical arguments about biological sensing superiority, and extensive impactful applications spanning robotics, healthcare, and autonomous systems. The paper calls for systematic research integration of adaptive sensing into embodied AI systems, proposing multimodal realtime frameworks, identifying challenges, and outlining research directions for the community.

### Strengths
1. The biological inspiration is well-motivated and provides an intuitive framework for understanding why adaptive sensing could be more efficient in some aspects.
2. The authors have effectively outlined the limitations and challenges, covering environmental sustainability, economic accessibility, generalization failures, and ethical concerns.
3. The potential integration of adaptive sensing in embodied AI contexts is very intriguing.

### Weaknesses
1. The paper primarily relies on computer vision classification task as the main empirical results to support the claims. While the Lens framework shows promising results, this represents evaluation on a narrow set of controlled scenarios. The lack of comprehensive evaluation across tasks, sensor/modality configurations, and real-world deployment conditions weakens the argument  for broad adoption.
2. The paper doesn't adequately address when and why adaptive sensing would outperform adaptive modeling approaches. Instead of controlling sensors, adaptation layers for diverse sensing inputs or models that generalize across domains might be more practical solutions. 
3. The authors do not sufficiently address the practical challenges of implementing adaptive sensing in existing AI pipelines. The hardware requirements, real-time computational overhead, and software infrastructure needs are mentioned but not thoroughly analyzed. This gap makes it difficult to assess the feasibility of the proposed paradigm shift beyond research prototypes.
4. Although Section 6 identifies key challenges, the response to the potential counterargument is relatively shallow.

### Questions
1. How could we systematically distinguish between cases where poor performance stems from sensor limitations versus model inadequacies?
2. Why does the framework require co-development of models and sensor strategies rather than treating adaptive sensor control as a separate, broadly applicable module? Could adaptive sensor parameter optimization be developed as a standalone component that works across different downstream models, similar to how data augmentation or preprocessing pipelines operate independently?
3. Given that domain adaptation, robust training methods, and model ensembling have shown significant success. When could adaptive sensing provides advantages over these alternatives? 
4. Can the authors discuss relevant real-time and deployment bottlenecks? 
5. The authors need to clarify when sensor limitations have been exceeded versus when model adaptation alone would suffice. A systematic analysis comparing sensor-level versus model-level adaptation would better justify the proposed approach and clarify when each strategy is optimal.

### Presentation
2

---

## Human Reviewer 3

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
The position paper argues for more adaptive approaches as a paradigm shift in AI/ML. In comparison model-based approaches that make predictions based on a static set of learned weights, adaptive sensing methods can optimize parameters (e.g., camera exposure or positioning) based on the input. A number of advantages of such methods are described in Section 3.2, and include more sample efficient learning (i.e., less training examples) and reduced uncertainty.

### Strengths
The position is states and the advantages and disadvantages of the position are described. The manuscript is generally easy to follow and understand.

### Weaknesses
The mathematics of reinforcement learning (RL) introduced in Section 5 is complex. In general, while the paradigm of adaptive sensing proposed in the introduction is very convincing, RL is just one of the ways how it can be accomplished. It wasn’t clear to me why the RL based approach is described in such detail then. Other approaches that the authors may consider include: 

Raisi (2019). Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. 

Maier (2018). Deep scatter estimation (DSE): feasibility of using a deep convolutional neural network for real-time x-ray scatter prediction in cone-beam CT.

These and other methods combine both physics-based modeling and AI to achieve the best of both worlds, using AI to accelerate slow computational processes in modeling, and can also be seen as adaptive sensing methods. In summary, I believe the paper would be much stronger if either the position was revised to only focus on RL or other, non-RL approach discussion would be incorporated into the manuscript.

### Questions
It is not clear how the proposed paradigm shift will take into account the proprietary nature of most sensors, i.e., it will be difficult to design such algorithms  when majority of manufacturers do not share details of their sensors. Moreover, the proposed shift may encourage any adaptive sensing AI algorithms to become proprietary (no model weights shared) themselves, negatively affecting AI transparency and safety efforts. 

An existing method (Lens [6]) is described. Are there other examples of adaptive sensing techniques that exist that are similar?

It is not clear if “adaptive” would refer to digital replicas of sensors that are rooted in physics/optics, or learning-based techniques that replicate the behavior seen in physical sensors.

### Presentation
3
