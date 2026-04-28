# Ferret-UI One: Mastering Universal User Interface Understanding Across Platforms

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 8, 6

## Abstract
Building a generalist model for user interface (UI) understanding is challenging due to various foundational issues, such as platform diversity, resolution variation, and data limitation. In this paper, we introduce \textbf{\model}, a multimodal large language model (MLLM) designed for universal UI understanding across a wide range of platforms, including iPhone, Android, iPad, Webpage, and AppleTV. Building on the foundation of Ferret-UI, \model{} introduces three key innovations: support for multiple platform types, high-resolution perception through adaptive scaling, and advanced task training data generation powered by GPT-4o with set-of-mark visual prompting. These advancements enable \model{} to perform complex, user-centered interactions, making it highly versatile and adaptable for the expanding diversity of platform ecosystems. Extensive empirical experiments on referring, grounding, user-centric advanced tasks (comprising 9 subtasks $\times$ 5 platforms), GUIDE next-action prediction dataset, and GUI-World multi-platform benchmark demonstrate that \model{} significantly outperforms Ferret-UI, and also shows strong cross-platform transfer capabilities. \blfootnote{$^\dagger$University of Texas at Austin. Work done during an internship at Apple. 
}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors present a model to recognize widgets on device screens, an evolution of a previously-published (in arxiv) model by Apple. The model performs better than the previous model, and slightly better than GPT-4o.

### Strengths
The paper is well written and fairly easy to understand. It provides a clear comparison with the previous version, what simplifies the reader's task of understanding what is novel.

The proposed model seems to perform significantly better than the previous one, in spite of greater generality. Its performance is comparable, if not slightly better, than GPT-4o.

### Weaknesses
Since the authors fail to disclose whether the model is going to be available, and how, it is hard to evaluate the impact and relevance for the community of the work described here.

Most importantly, since most of the improvements are engineering-related, the main take-away of the paper is that Ferret-UI, a paper which was never peer-reviewed, can be improved. In other words, there is not much novelty here, beyond knowing it can be done, since the methods used are quite straight-forward.

Notice that the performance of the model is probably still too low to make it useful. It fails elementary and ground tasks at the rate of 1 and 5, that is, in most screens it will be incorrect in relation to at least one widget. This is probably too much for any serious attempt to connect it to an agent, at least in a safe way. In fact, a more interesting and useful benchmark is how successful such models are in actually interacting with a screen, but this is beyond this paper.

### Questions
1. What do you think are the scientific contributions of this paper? How much of it is just good engineering of tested ideas?
2. How is this model going to be made available to researchers and developers?
3. What would you consider a "usable" performance of a model like Ferret-UI?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Edit: Updated Review based on Feedback from Associate Program Chairs

This paper introduces Ferret-UI One, a multimodal large language model designed for universal UI understanding across multiple platforms including iPhone, Android, iPad, Web, and AppleTV. The key innovations are threefold: multi-platform support through unified data collection and processing, high-resolution perception through an adaptive N-gridding mechanism, and advanced task training data generation using GPT-4o with set-of-mark visual prompting. The authors demonstrate the model's effectiveness through comprehensive evaluations on elementary tasks, advanced tasks, and public benchmarks like GUIDE and GUI-World.

### Strengths
The paper's technical contributions are well-motivated. The adaptive N-gridding mechanism provides an elegant solution to handling varying resolutions while maintaining bounded computational costs, with clear mathematical formulation in Algorithm 1. The set-of-mark visual prompting approach for GPT-4o data generation represents an acceptable way to improve spatial understanding in training data generation, addressing a key limitation of previous text-only prompting methods.
The authors conduct extensive experiments across multiple platforms and task types, providing strong baseline comparisons including GPT-4o and previous state-of-the-art models. The ablation studies examining cross-platform transfer capabilities and architectural components offer valuable insights into the model's behavior. Particularly noteworthy is the model's strong performance even with smaller variants like Gemma-2B, suggesting practical applicability.
The paper addresses a genuine need in the field for universal UI understanding across diverse platforms. The demonstrated zero-shot generalization capabilities, especially in the GUI-World benchmark results, indicate robust real-world applicability.

### Weaknesses
A significant concern is the severe data imbalance across platforms, as evident in Table 1. The web platform dominates with 321k images, followed by iPhone with 112k images, while iPad and AppleTV have only 19k and 16k images respectively. Though the authors acknowledge this limitation and mention mitigation strategies like loss weighting and targeted task generation, the effectiveness of these approaches isn't thoroughly analyzed or quantified. To mitigate this, the answer is in balancing the data used across devices.

The methodological analysis has several gaps. The paper lacks a detailed examination of failure cases or systematic error analysis. There's limited discussion of computational requirements and inference speed comparisons across different platforms and resolutions. (for model it'll be specific, but in UI design, speed is a major element and latency numbers there would be helpful). Inference speed and overall latency in milliseconds is be a good metric. Additionally, potential biases in GPT-4o generated training data aren't thoroughly explored (although I consider it to be out of scope of this paper), which could impact the model's generalization capabilities.

The experimental design could be more rigorous. The cross-platform transfer results presented in Table 4 would benefit from error bars / error spread measures. Wherever appropriate, provide confidence intervals / standard deviations and running the experiment multiple times to ensure reliability.

### Questions
2. Can you provide detailed examples of failure cases, especially for low-resource platforms like AppleTV?
3. How does the quality of GPT-4o generated training data vary across platforms, and are there systematic differences in generation quality?
4. What are the inference time comparisons between platforms for Ferret-UI 1 ?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces an MLLM-based GUI Agent aimed at enhancing user interface (UI) understanding across a wide range of platforms. These platforms include mobile devices (iPhone, Android), tablets (iPad), web pages, and smart TVs (AppleTV). The paper builds on previous work, Ferret-UI, proving its efficacy on referring, grounding, and advanced user-centric tasks, showing significant improvements over the previous Ferret-UI model and other benchmarks like GUIDE and GUI-World.

### Strengths
- **Multi-platform Support**: One of the paper's key strengths is the successful integration of multiple platforms (iOS, Android, web, smart TVs), making the model more versatile in various user environments. The authors also discuss the transfer learning effects of each platform.
- **Advanced Task Training with GPT-4o**: The use of GPT-4o with visual prompting for training data generation significantly enhances the model’s performance, particularly on complex tasks requiring spatial understanding of UI components.
- **Strong Empirical Results**: The results presented in the paper indicate that Ferret-UI One outperforms its predecessor, Ferret-UI, across several metrics, including grounding, referring, and advanced task handling, particularly on the GUIDE and GUI-World benchmarks.
- **Zero-shot Transfer**: The model demonstrates robust zero-shot performance, indicating that it generalizes well across different platforms without overfitting to training data, a key advantage for building scalable UI systems.

### Weaknesses
 - **Extra Probing for Models Potential**: This paper mainly follows the pipeline of GUI-world, proposing a multi-platform GUI agent by collecting the dataset first and annotating it with SOTA MLLM GPT-4o. Although its performance is SOTA in GUI-World and GUIDE benchmark, the whole paper is not that exciting to me.  I think your model's experiment results are expected to be superior to Ferret-UI because Ferret-UI One is trained on more high-quality instruction tuning and task-specific data. The authors are suggested to probe more potential capability of their models such as the grounding plugin for general MLLM-based GUI Agents in benchmarks such as OS-world or VisualAgentBench. 
- **Evaluation and Analysis of Synthetic Dataset**: The authors are suggested to evaluate whether GPT-4o can perform the annotation task well by providing some quantitative results. Moreover, a comprehensive comparison to previous GUI datasets and analysis of your dataset is needed.
- **Case Study**: Show more case studies in the appendix and provide failure cases of Ferret-UI One in GUIDE and GUI-World in grounding and navigation tasks for a more comprehensive review of your proposed model, as well as an analysis of why your model fails. A more detailed discussion of future direction is also suggested on topics of building more general agents across various platforms or how to improve the grounding or navigating capabilities of current models or agents.
- **Additional Experiments**:  I think authors can include more comparative baselines to show the strength of your synthetic data generation pipeline. The authors can consider SeeClick and SeeClick-V on your proposed benchmark, two strong baseline models in REC, grounding, and navigation tasks because these models are all recently released and show high potential in GUI grounding tasks. Another option is to evaluate your model in popular GUI grounding benchmark ScreenSpot proposed in SeeClick.

### Questions
See Weakness Above.

### Soundness
2

### Presentation
3

### Contribution
3
