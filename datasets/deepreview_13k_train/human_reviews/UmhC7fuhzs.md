# Skin, Muscles, and Bones in MultiSensory Simulation

- Decision: Reject
- Scores: 6, 6, 6, 8

## Abstract
General-purpose household robots require real-time fine motor control to handle delicate tasks and urgent situations. In this work, we introduce the senses of proprioception, kinesthesia, force haptics, and muscle activation to capture such precise control. This comprehensive set of multimodal senses naturally enables fine-grained interactions that are difficult to simulate with unimodal or text conditioned generative models. To effectively simulate fine-grained multisensory actions, we develop a feature learning paradigm that aligns these modalities while preserving the unique information each modality provides. We further regularize action trajectory features to enhance causality for representing intricate interaction dynamics. Experiments show that incorporating multimodal senses improves simulation accuracy and reduces temporal drift. Extensive ablation studies and downstream applications demonstrate effectiveness and practicality of our work.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a method for improving generative simulations in household robots incorporating multisensory inputs such as proprioception, kinesthesia, force haptics, and muscle activation. These sensory signals support delicate, real-time control essential for tasks involving fine motor skills.

The authors introduce a feature learning paradigm that aligns sensory modalities in a shared representation space while retaining each modality's unique contributions. A regularization scheme enhances causality in action trajectories, allowing for a more accurate representation of interaction dynamics.

The model achieves improvements in simulation accuracy and reduced temporal drift, outperforming baseline models. Comprehensive experiments and suggested applications, such as policy optimization and planning, demonstrate the model’s effectiveness in downstream applications

### Strengths
1. This work integrates multimodal information into generative simulations (video generation), addressing a reasonably novel task. The proposed pipeline effectively tackles multimodal misalignment using cross-attention, channel-wise softmax, and relaxed hyperplane interaction.

2. Extensive experiments show reasonable improvements over the previous state-of-the-art method, UniSim, across four metrics (MSE, PSNR, LPIPS, and FVD), with consistent improvements across different prediction time spans.

3. The ablation study confirms the effectiveness of using various modality data and validates different design choices. Interesting findings include a high correlation between hand force and muscle EMG data.

4. Clear visualizations in both the main paper and appendix enhance understanding of the method and results.

### Weaknesses
1. The model is trained solely on the ActionSense dataset, which limits the generalizability of the results. The ActionSense dataset, while useful for its multimodal data, may not capture the full range of variations present in real-world robotic manipulation scenarios. This raises concerns about the model's ability to perform well on tasks involving different objects, environments, or interaction styles.

2. The experiments are conducted with 64x64 resolution videos, which may be too low for real-world applications, such as robotic manipulation. Such low resolution can obscure fine details critical for precise control, such as the exact position of fingers or the subtle changes in object shape during manipulation. This limitation could hinder the model's applicability to tasks requiring high visual fidelity.

3. Some experiments are incomplete: in Table 3, the "Ours with sentence" result is missing, which would strengthen the study. The absence of this result makes it difficult to fully assess the impact of incorporating sentence-level information into the model. This missing data point weakens the overall analysis of the model's performance across different input modalities.

### Questions
1. Since in Table 1. there is some result in missing some of the domain data, could the proposed method apply to out-of-domain videos without multimodal information, such as the EpicKitchen dataset?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach to multisensory simulation for fine motor control in general-purpose household robots. By introducing proprioception, kinesthesia, force haptics, and muscle activation, the authors aim to enhance generative video simulation models to better capture delicate control tasks. They propose a multimodal feature extraction paradigm that aligns sensory data to a shared representation space while preserving unique modality information. Additionally, a feature regularization method is introduced to enhance causality in action trajectory representations. The paper evaluates the model using the ActionSense dataset, demonstrating improvements in simulation accuracy and temporal consistency.

### Strengths
1. Originality: The introduction of a comprehensive set of interoceptive signals for generative simulation is novel, providing an innovative alternative to unimodal and text-based approaches in robotic control.
2. Quality: The method demonstrates clear improvements over baselines, especially in reducing temporal drift and enhancing fine-grained control, validated through detailed quantitative metrics and ablation studies.
3. Clarity: The experimental section is well-organized, allowing readers to understand the evaluation metrics and the comparative advantage of the proposed approach. Figures effectively illustrate the model’s performance across different sensory configurations.
This multisensory approach holds value for robotics, especially in applications requiring high-fidelity simulations for complex tasks, such as culinary or surgical activities, where precise control is essential.

### Weaknesses
1. The paper's reliance on a single dataset, ActionSense, restricts the method's demonstrated applicability. The dataset’s constraints—kitchen-based activities with a limited range of sensory inputs—limit the model's robustness across more varied settings. Extending the model's evaluation to diverse datasets involving different environments or robotic tasks would enhance its generalizability and applicability to real-world scenarios
2. Evaluation Scope: While the chosen metrics (MSE, PSNR, LPIPS, FVD) are appropriate for measuring video quality and temporal consistency, they do not address practical performance aspects such as the real-time execution capability on hardware-constrained robotic systems. Additionally, the experiments are limited to low-resolution (64x64) video output, which restricts the findings’ relevance for applications requiring high-fidelity visualizations. Testing on higher resolutions and considering hardware performance would strengthen the claim of practical applicability​.
3. Experimental Setup: The paper uses only subject five from ActionSense for testing while training on other subjects. This setup risks potential overfitting to specific motion patterns of a single subject, limiting cross-subject generalization. Cross-validation across subjects would help confirm the model’s robustness across various human motion characteristics​.

### Questions
1. Handling of Missing Sensory Modalities
Could the authors elaborate on the model's performance and stability when one or more sensory modalities are absent during testing? While the model’s robustness to missing modalities is briefly explored, further quantitative insights or analysis would strengthen the claim of adaptability. For real-world robotic applications, understanding how effectively the model compensates for missing inputs, such as through predictive mechanisms or alternative sensory weighting, would clarify its resilience to potential sensor failures.
2. Evaluation Beyond the ActionSense Dataset
The model’s evaluation is currently limited to ActionSense, which may not cover the full range of real-world tasks or interactions. Has any additional testing on varied datasets or environments been considered, or might it be feasible to cross-validate the model on similar multimodal datasets to confirm generalizability? Testing the model across broader contexts, such as more diverse daily activities or complex motor tasks, could reinforce its suitability for a wide range of applications and help mitigate dataset-specific limitations.
3. Computational Feasibility and Real-Time Constraints
Given the goal of deploying this approach in robotic applications, has any analysis been conducted on the model’s computational efficiency, especially in real-time or edge-computing scenarios? Insights on its processing requirements, latency, or suitability for deployment on constrained hardware would provide a clearer picture of its practicality. Specifically, understanding whether the model’s complexity scales with resolution or with the number of modalities would help determine the trade-offs between sensory input fidelity and processing efficiency.
4. Temporal Consistency and Model Drift Over Extended Simulations
While temporal drift reduction is highlighted as a strength, could the authors clarify the model’s performance stability in longer-term simulations or scenarios where prolonged fine motor control is needed? Given that robotic tasks often require sustained, accurate control, exploring how well the model mitigates accumulated drift over extended timeframes would enhance understanding of its practical performance in continuous operations.
5. Comparative Analysis with Multimodal Baselines
The paper mentions baseline comparisons with several multimodal feature extraction paradigms but does not provide a qualitative analysis of where the proposed model outperforms or falls short relative to these baselines. Would the authors consider offering a more detailed comparative breakdown, perhaps by examining specific cases where other methods fail or by isolating scenarios in which the proposed approach shows the most notable improvements? This comparison would be valuable in delineating the unique benefits of the model’s design choices. 
Thank you for considering these questions and suggestions. I look forward to your responses, which I believe will further highlight the strengths and clarify the broader applicability of your approach！

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a multisensory approach for generating videos, where proprioceptive, kinesthetic, force haptic, and muscle activation data are used to condition a video diffusion model that synthesizes realistic frames. Key contributions include a multimodal feature extraction paradigm and a novel regularization scheme to enhance the causality and alignment of action trajectories in the latent space. Using the ActionSense dataset, the authors demonstrate that multisensory input enhances prediction accuracy and temporal consistency compared to unimodal conditioning.

### Strengths
- This approach addresses significant gaps in current video prediction methods, particularly for videos involving fine-grained motor movements.
- The regularization applied in the latent space is shown to improve model performance, potentially enhancing prediction stability and the temporal alignment of generated frames.
- This framework could advance simulators for fields requiring multisensory input, such as robotics or motor skill training. Integration of proprioceptive and haptic data improves video generation performance, which could support downstream tasks such as adaptive control policy development.

### Weaknesses
 - The explanation of core processes—multisensory feature fusion, latent regularization, and video diffusion configuration—is often vague. Terms and subscripts are not well defined, making it difficult to follow some derivations and mechanisms. Similarly, the introduction and other parts of the text can be improved. Additionally, figures lack arrows or labels that would clarify data flow, and some of the text within illustrations is too small.
- It's not clear the effectiveness of multisensory integration compared to the other proposed mechanisms. In particular, the ablation study reveals a minimal performance drop when some sensory modalities are removed at test time, suggesting unexpected redundancy. Table 2 shows that the model with a single modality (e.g., hand-force only) can still achieve high performance, raising questions about the true necessity of multisensory inputs compared to other mechanisms at play. For example, hand and body pose data seem to be crucial but can be removed at test-time with minimal impact on LPIPS scores, which is counterintuitive and requires further investigation.
- This approach depends heavily on multisensory datasets, which are often costly and difficult to obtain in real-world settings. Applications would require large-scale "in-the-wild" data to achieve generalization, limiting the method’s accessibility. 
- The paper primarily compares performance variations within its own framework but lacks comparisons to integrate multi-sensory modality with other baselines (e.g., Mutex, LanguageBind, ImageBind).
- The low-level policy optimization with the current simulator is not clearly articulated, specifically the difference between the baseline and the policy with the simulator.
- While the multisensory conditioning approach improves the performance, the model would benefit significantly from the ability to predict multisensory outputs in addition to visual frames. Predicting proprioceptive, kinesthetic, and haptic feedback could open up for multiple applications, where accurate multisensory feedback is essential.

### Questions
- Consider revisiting the title to more accurately reflect the multisensory conditioned video generation aspect, as the current title may be misleading.
- Why were the specific baseline models chosen, and how do they differ fundamentally from the current method? If these methods were augmented with multisensory data, would they perform comparably?
- In unimodal tests, is cross-attention with video features and action regularization also employed? Is the number of modalities the only thing that differs in these comparisons?
- How does performance change when multiple modalities are removed (similar to Table 2)? In particular, when does the model leverage co-interaction between modalities? It would be good to have a more comprehensive ablation study showing performance across possible combinations of modalities.
- How does computational efficiency scale with additional sensory inputs? How does that affect computation time and memory usage?
In policy optimization, how does the policy generate frames when the proposed simulator is removed? It’s not clear the comparison with the baseline policy
- Did the authors consider adding the capability to predict multimodal sensory outputs? What are the potential challenges? This would significantly extend the application and contribution of this work.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors proposed a multisensory action presentation learning for generatively simulating videos with fine-grained manipulation. They introduced a multimodal feature extraction paradigm to align modalities including haptic forces, muscle stimulation, hand and body poses. They also proposed a generative simulation method by using the aligned multimodal action representation for fine-grained control of a video diffusion simulator. They evaluated the propose method with extensive ablation studies and comparison with previous work, and also demonstrated the applications in policy learning and planning.

### Strengths
This work is well-motivated to leverage multimodal sensory measurements to simulate fine-grained control. The problem is well-formulated and the proposed approach is well-explained with great details. The work has thorough and concrete experiments and evaluations.  Both  quantitive and qualitative results are presented with analysis. I believe the system can be adapted by further researchers.

### Weaknesses
I assume all tests were conducted within the same domain as the training set, such as the data were recorded when the demonstrators were doing the similar tasks with similar tools, or equipped the sensors in the same way.  I wonder how generalizable the proposed method can be? Such as what if having a different background, using a tool with different shape or color, cutting different vegetables/fruits?

1. Section 2.1. About the cross attention: What is z_{t, m, j} and is it used anywhere else?
2. Section 2.2 Relaxed Hyperplane Interaction: The sentence “A geometric interpretation of the latent interaction… depicts two space partitioned by a hyperplane defined by …” was confusing to me. Could you explain it with more details?
3. Section 2.2 Relaxed Hyperplane Interaction: L_{VDM} was used before its definition.
4. Fig 3 and Fig 6. (a) Please highlight the best results for each column.  (b) Please explain what LPIPS is in the figure caption. Note: it would be great if all figures are self-contained with short explanations in caption. 
5. Please highlight the best/the best two results for each column in Table 1.
6. Section 3.1 Comparison with Text-conditioned Simulation: typo “Phrasse” -> “Phrase”
7. How many tasks are there in the dataset? And what are these?
8. Figure 15: Should Top right be Failure cases and Top left be additional qualitative results?

### Questions
1. Section 2.1. About the cross attention: What is z_{t, m, j} and is it used anywhere else?
2. Section 2.2 Relaxed Hyperplane Interaction: The sentence “A geometric interpretation of the latent interaction… depicts two space partitioned by a hyperplane defined by …” was confusing to me. Could you explain it with more details?
3. Section 2.2 Relaxed Hyperplane Interaction: L_{VDM} was used before its definition.
4. Fig 3 and Fig 6. (a) Please highlight the best results for each column.  (b) Please explain what LPIPS is in the figure caption. Note: it would be great if all figures are self-contained with short explanations in caption. 
5. Please highlight the best/the best two results for each column in Table 1.
6. Section 3.1 Comparison with Text-conditioned Simulation: typo “Phrasse” -> “Phrase”
7. How many tasks are there in the dataset? And what are these?
8. Figure 15: Should Top right be Failure cases and Top left be additional qualitative results?

### Soundness
3

### Presentation
3

### Contribution
3
