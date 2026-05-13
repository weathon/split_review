# Control-oriented Clustering of Visual Latent Representation

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
We initiate a study of the geometry of the visual representation space ---the information channel from the vision encoder to the action decoder--- in an image-based control pipeline learned from behavior cloning. Inspired by the phenomenon of \emph{neural collapse} (NC) in image classification~\citep{papyan2020prevalence}, we \rv{empirically demonstrate the prevalent emergence of a similar \emph{law of clustering} in the visual representation space. Specifically, 
\begin{itemize}
    \item In \emph{discrete} image-based control (e.g., Lunar Lander), the visual representations cluster according to the natural discrete action labels;
    \item In \emph{continuous} image-based control (e.g., Planar Pushing and Block Stacking), the clustering emerges according to ``\emph{control-oriented}'' classes that are based on (a) the relative pose between the object and the target in the input or (b) the relative pose of the object induced by expert actions in the output. Each of the classes corresponds to one \emph{relative pose orthant} (\repo).
\end{itemize}
}
Beyond empirical observation, we show such a law of clustering can be leveraged as an \emph{algorithmic tool} to improve test-time performance when training a policy with limited expert demonstrations. Particularly, we \emph{pretrain} the vision encoder using NC as a \emph{regularization} to encourage control-oriented clustering of the visual features. Surprisingly, such an NC-pretrained vision encoder, when finetuned end-to-end with the action decoder, boosts the test-time performance by $10\%$ to $35\%$. Real-world vision-based planar pushing experiments confirmed the surprising advantage of control-oriented visual representation pretraining. \footnote{\url{https://computationalrobotics.seas.harvard.edu/ControlOriented_NC}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies neural collapse for control tasks. To facilitate this study, the authors learn policies with behavior cloning end-to-end. To probe the learned representations, they define a heuristic classification of features learned within the encoder called REPOs that categorize the position and orientation of the object in the image relative to the target object (this is specific to planar push tasks). They find that pretraining the vision encoder using neural collapse as a regularization technique improves performance on a simulated and real-world push-t task. They also find that, when the model is continually fine-tuned on different planar push tasks, the visual representation space undergoes re-clustering instead of saturating on early training tasks.

### Strengths
To my knowledge, this is the first paper to study neural collapse in control. I appreciated some of the unconventional writing choices. The introduction had a nice unification of optimal control and behavior cloning and made the relevance of neural collapse to control very apparent. The experimental approach was really unique, creative, and insightful. The continual learning findings were especially interesting from my perspective.

### Weaknesses
The paper could benefit from a more concise abstract and a more broad introduction that provides stronger motivation for the problem and clearer articulation of the paper's contributions. I like the unconventional approach to the abstract, but it would be more clear to the audience if the toy experiment appeared as a preliminary to the method section. 

I took issue with the discussion of resnet features throughout the paper. 
- First in response to L213: pre-trained resents are still useful compared to randomly initialized models, and second, that fine-tuning is often required for many transfer learning tasks, so I don't find it surprising that we need to fine-tune imagenet trained resnets for control domains.
- Because the image input of push-t is so limited it's unfair to make broad claims about the utility of resnet features. The benefit of resnet features will be more apparent in more visually challenging settings (e.g., cluttered table-top manipulation).

Overall, as a study of visual representations the findings need to be verified on more visually complex domains.

Typo: "Expect" instead of "expert" on line 118.

### Questions
Can you validate these findings on more visually complex domains?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates whether the phenomenon of neural collapse, previously observed in image classification and other tasks, appears in visual representations trained for continuous control. The paper considers the setup of training a visual encoder end-to-end jointly with a behavioral cloning policy on a planar pushing task. To study it as a classification problem, the frames are binned by relative poses to future states. The paper shows that during end-to-end training, the visual representation undergoes neural collapse. Finally, the neural collapse metrics are used as a regularization objective to improve downstream behavioral cloning performance.

### Strengths
- The study of neural collapse in the visuomotor control setting is novel and well-motivated.
- The minimum-time double integrator example is very clear.
- Sim and real experiments show that neural collapse regularization objectives improve downstream task performance.
- Fine-tuning experiments show that neural collapse happens when transferring across domains.

### Weaknesses
 - It seems unclear if the downstream improvement is from the NC regularization itself, or from access to ground truth state (by proxy of the class labels).
- The criteria for determining whether neural collapse has occurred seems unclear in this setting. Specifically, it's not clear how the CDNV, STD Angle, and STD Norm metrics relate to the concept of neural collapse, and why these metrics are expected to tend to zero. Moreover, the figures presented do not show these metrics converging to zero, which raises questions about the interpretation of the results.
- How sensitive is the observation of neural collapse to the choice of clustering? The hypothesis that the visual representation conveys a goal to the action decoder seems arbitrary. For example, one could also posit that the visual representation encodes the current environment state (block and EE pose). What happens if we cluster on environment state? Do we still observe neural collapse? What if we assign class labels uniformly at random? It would be convincing to see these comparisons as a justification for this choice.
- If the core claim is that neural collapse happens for visual encoders trained end-to-end in control tasks, it could perhaps be clearer and more convincing to apply this first to discrete control, and show that neural collapse in visual representation occurs across various discrete control environments like CartPole, etc.

### Questions
- In Table 1, is the performance improvement from access to privileged information (ground truth state), or from the NC regularization itself? It would be good to see a baseline where the orthant class label is provided as input to the policy alongside the image embedding, but no NC regularization is used.
- Could you clarify what constitutes neural collapse when we look at CDNV, STD Angle, STD Norm? In line 293-304, it is stated that these metrics should tend to zero as an indicator of neural collapse. However, in the figures below, none of the metrics seem to tend to zero.
- How sensitive is the observation of neural collapse to the choice of clustering? The hypothesis that the visual representation conveys a goal to the action decoder seems arbitrary. For example, one could also posit that the visual representation encodes the current environment state (block and EE pose). What happens if we cluster on environment state? Do we still observe neural collapse? What if we assign class labels uniformly at random? It would be convincing to see these comparisons as a justification for this choice.
- If the core claim is that neural collapse happens for visual encoders trained end-to-end in control tasks, it could perhaps be clearer and more convincing to apply this first to discrete control, and show that neural collapse in visual representation occurs across various discrete control environments like CartPole, etc.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates whether visual features in image-based robotic control systems exhibit neural collapse (NC) - a clustering phenomenon previously observed in image classification tasks where features group into distinct classes. The authors find that on robotic control task of planar pushing, the visual features do indeed cluster into eight "control-oriented" classes based on relative pose between objects and targets. Most importantly, they show this clustering behavior can be leveraged to improve robot performance by up to 35% in low-data scenarios by pretraining the visual encoder to encourage such clustering, demonstrating benefits in both simulated and real-world robotic pushing tasks.

### Strengths
1. I like the interpretable way of converting a regression task (in the context of behavior cloning) of action prediction to (x, y, $\theta$), which can be discretized.

2. It is interesting to see that the authors have included experiments on a real robot for the task of planar pushing and especially the boost that pretraining to minimize NC metrics gives compared to the baseline.

### Weaknesses
3. The introduction can have more motivation of what NC is and why and where is this phenomenon observed rather than elaborating too much on the toy example. For instance, in the **Our goal** paragraph (L112), the authors raise the question "Does a similar law of clustering, in the spirit of NC, happen when cloning image-based control policies?" However, it is not very clear at this point on why this clustering is important to begin with? What happens if my control policies are working well and aren't clustered in the spirit of NC? Why should the reader care. Specifically it'd be good if authors can add the following:
	- Explicitly state potential benefits of finding NC in control policies (e.g. improved generalization, more interpretable features)
	- Expand on why clustering in the visual representation space might be important for control policies, even if they are already working well

4. In addition to this the related works is pushed to the appendix giving the reader a hard time to contextualize the current work. I'd highly suggest rewriting the related works as well as the motivation/introduction to address #1.

5. Fig 5 is really hard to read. Can't the plots for the 4 methods (ResNet/DinoV2 + LSTM/DM) be combined into a single plot for each of the 3 metrics (CDNV, STD Angle, STD Norm), resulting in 3 plots? 

6. Can the authors visualize (x, y $\theta$) for the 4 methods during testing policy rollouts in a 3D space as that was the main driving point for proposing REPO (L260)?

### Questions
7. Will the results shown for planar pushing generalize for other robotic manipulation tasks such as Lifting Cube or Stacking cubes? There are several simulators such as Robosuite that provide with demonstrations of such task -- can REPO be extended to these non-planar tasks in a trivial manner or is it a future avenue of research?

8. Some results in Sec 3.1 (finetuning experiments), are not new. Observation (i) is stated as "During retraining on the target domain, performance increases in the target domain but drops in the source domain." -- Isn't this true for deep learning networks in general? 

9. Why aren't DinoV2 features also used for Table 1 (i.e pretraining DinoV2 to minimize NC metrics) and using that for control policies?

10. What is the Baseline model architecture that is used in Table 1?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates the geometry of the visual representation space in an image-based control pipeline trained through behavior cloning, focusing specifically on planar pushing tasks. It explores whether a phenomenon similar to neural collapse (NC), originally observed in image classification, can emerge in a regression context such as control tasks. The authors introduce "control-oriented" classes based on the relative poses of objects and targets, or relative poses of objects at different time steps, leading to the following key findings:
1. Control-oriented clustering emerges in the visual representation space, with latent features forming clusters according to control-relevant classes.
2. Using NC as a pretraining strategy for the vision encoder improves test-time performance, particularly when training data is limited.
3. Real-world experiments validate the effectiveness of NC pretraining in enhancing control performance.

### Strengths
1. Novel and interesting results: The paper presents intriguing and slightly surprising results, showing that control-oriented clustering in visual representations emerges even though the planar pushing task involves continuous control signals. Additionally, it demonstrates that pretraining the visual encoder improves test-time performance when training with limited expert demonstrations.
2. Excellent presentation and writing: The presentation of this paper is clear and engaging. The authors begin with a motivating toy example that introduces the phenomenon of NC, then proceed to answer two key questions: (a) Does NC occur in the visual representation space? and (b) Is the extent of NC related to model performance? The arguments are supported with convincing evidence, and the writing is very easy to follow.
3. Real-World Validation: The paper includes real-world experiments on vision-based planar pushing to show the effectiveness of NC pretraining

Overall, this paper presents novel and interesting results, with clear presentation and strong supporting evidence. This paper also opens up lots of future research directions in visual representation learning for robotics control, which will greatly benefit the community. This paper is clearly above the acceptance bar for ICLR.

### Weaknesses
1. Scalability of the proposed approach for more complex tasks: Leveraging NC for control requires manually specified class definitions. In the planar pushing task, these classes are defined using the ground-truth relative pose of the target position with respect to the object, or the relative pose of the object at time t+H with respect to the object at time t. These classes are easy to define because the T-pushing task involves a single object, and its pose can be easily estimated using an AprilTag attached at the bottom of the T. However, the same class definition and pre-training strategy may not apply to more complex real-world tasks. In real-world robotic applications with diverse objects, accurate pose estimation can be challenging, particularly for deformable objects where defining a canonical pose is difficult. While accurate pose estimation is not the focus of this paper, it would be beneficial to discuss the potential limitations of the proposed class definitions in scaling to more complex tasks, or consider possible alternative class definitions. Specifically, the paper does not address how the method would handle scenarios with multiple interacting objects, occlusions, or partial observability, which are common in real-world manipulation tasks. The reliance on precise pose information, which may not be readily available or accurate in complex environments, is a significant limitation.
2. Limited pretraining details and ablation studies: The paper lacks details about the visual pre-training, such as training datasets and training schedules. Moreover, there are no ablation studies provided on the relative importance of the two NC metrics in pretraining. Without these details, reproducing the results from the paper is challenging. Including such information would improve the reproducibility and robustness of the findings. For example, the paper does not specify the exact architecture of the vision encoder used, the size of the training dataset used for pretraining, or the learning rate and batch size used during pretraining. Furthermore, it is unclear how the hyperparameters for the NC loss were chosen, and whether the performance is sensitive to these choices. The lack of ablation studies on the individual components of the NC loss makes it difficult to assess their relative contributions to the overall performance improvement.

### Questions
Why does the clustering phenomenon emerge for the planar pushing task with a continuous control signal? The toy example has discrete states in the closed-form optimal policy, so one can see why the clustering phenomenon might arise. The planar pushing task presents a different scenario where this emergence seems less intuitive.

### Soundness
4

### Presentation
4

### Contribution
4
