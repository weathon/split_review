# A closed-loop EEG-based visual stimulation framework from controllable generation

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 8, 6, 3

## Abstract
Recent advancements in artificial neural networks (ANNs) have significantly refined methodologies for predicting the neural coding activities of the ventral visual stream in human and animal brains based on visual stimuli. Nevertheless, the endeavor to control visual stimuli to elicit specific neural activities continues to confront substantial challenges, including prohibitive experimental costs, the high-dimensional nature of stimuli, pronounced inter-individual variability, and an incomplete understanding of neuronal selectivity. To address these impediments, we propose a novel electroencephalography (EEG)-based closed-loop framework for visual stimulus. Leveraging this framework, we can identify the optimal natural image stimulus within a theoretically infinite search space to maximize the elicitation of neural activities that most closely align with desired brain states. Our framework employs advanced ANN ensemble models to ensure the reliability of neural activity predictions. Furthermore, we conceptualize the brain coding predicted by the ANN model as a non-differentiable black-box process, allowing us to directly analyze the relationship between the administered visual stimuli and the targeted brain activity. Our research demonstrates that, independent of the exactness of the ANN-predicted brain coding, the proposed framework can procure the theoretically optimal natural image stimulus at given cycle steps. Moreover, our method exhibits generalizability across different modalities of brain-specific activity regulation. Our code is available at https://anonymous.4open.science/status/closed-loop-F2E9.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper develops a method for choosing the optimal image stimulus to present to a human subject to elicit a specific desired pattern of neural activity (as measured using EEG).

### Strengths
The problem that this paper takes on is very interesting. I am aware of previous research that has attempted to find preferred visual stimuli for single neurons, so as to figure out what that neuron "prefers", but this paper seems to be taking on a related but quite different issue, which is: given a whole pattern of population activity, what stimulus would elicit that overall pattern? This seems like a project that may have useful clinical applications in the future, as well as being scientifically interesting in its own right.

### Weaknesses
I found the paper hard to follow. I admit that a contributing factor here may be my own lack of experience with respect to some of the techniques the paper uses, such as EEG data, diffusion models, and genetic algorithms. However, I do think that the presentation of the paper could be much clearer, and I will list some examples below of specific issues that came up with respect to clarity.

- Most of the figures I did not understand, and as far as I could tell, the figures aren't referred to in the main text, so it was difficult to situate what the purpose of each figure was in the overall narrative of the paper. 
- It is unclear what the purpose of the MDP is in Section 3.2 (see Questions below).

It would probably have been useful to include a Supplemental section to explain some of the methods in more detail.

### Questions
In Sec 3.2, what do the actions and states of the MDP refer to in this context? Are the actions features, because the algorithm is selecting features of the neural activity to represent? Or are the actions the selected images to be used as visual stimuli? 

What is the motivation for not updating the gradients in the model? The abstract says this allows "us to directly analyze the relationship between the administered visual stimuli and the targeted brain activity", but I wasn't sure why this is the case or where in the paper this motivation is fully explained or justified.

In Figure 1, what is the difference between "selection" and "action"?
In Fig 2, the distance metric seems to be applied to images, but I thought the point was to compare induced and target neural activities.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This is a highly innovative study demonstrating the capability to identify visual stimuli that closely match the original stimuli eliciting specific EEG activity patterns. The algorithm is well-explained and, to my knowledge, represents one of the first successful applications of this approach with EEG data.

### Strengths
Very interesting study, timely, solves an important question, is generalizable.

### Weaknesses
I can hardly identify any significant limitations in the current study. However, I have two questions:

The authors state that the identified stimulus is "optimal." Based on the MDP formulation of the algorithm, I understand that it finds a local minimum. Could you clarify how this approach ensures finding a global optimum, rather than a local one?

Why did you limit the comparison to the first 250 ms (Figure 4D)? While the initial 250 ms may indeed capture critical visual information, it is common in EEG analysis to display the full 1000 ms post-stimulus data. Could you elaborate on this choice?

### Questions
The authors state that the identified stimulus is "optimal." Based on the MDP formulation of the algorithm, I understand that it finds a local minimum. Could you clarify how this approach ensures finding a global optimum, rather than a local one?

Why did you limit the comparison to the first 250 ms (Figure 4D)? While the initial 250 ms may indeed capture critical visual information, it is common in EEG analysis to display the full 1000 ms post-stimulus data. Could you elaborate on this choice?

### Soundness
4

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
4

### Summary
The authors proposed a closed-loop stimulation framework for EEG-based visual encoding, aiming to generate visual stimuli to elicit specific neural activities through controllable image generation strategy. In this framework, the authors control the stimulus image generation by approximating the brain activity evoked by the visual stimulation towards the desired neural response that corresponds to the candidate images rated by human users iteratively. Controlling visual stimuli in visual encoding studies is very important. Meanwhile, the stimulus images in most prior studies are relatively arbitrary as there is no standard criteria. The proposed framework provides a possible solution to this problem.

### Strengths
The proposed closed-loop framework for synthetic visual stimuli generation in novel in several ways, in terms of the retrieval strategy for identifying candidate images, the feature selection approach, and the method to addressing the problem of unknown target query image. The framework and related methodologies are well designed and presented in general.

### Weaknesses
The weaknesses of the manuscript lie in the lack of details and validations. For example, the details of encoding model are not sufficient. The authors described the architecture of the encoding model, however, the details for training such an encoding model is missing. he authors should provide details about training procedure, including data sources. Was the encoding model trained using data from multiple subjects or was it subject-specific? What is the method to validate the encoding model? More importantly, the encoding model was not adequately validated (at least I didn’t see any results related to the encoding model) given its critical role in the framework. In addition, what are the criteria and how to validate that the synthetic images are the “optimal” subset that can evoke specific neural activities? Similar issues exist in other modules, e.g., feature selection and interactive search. The authors are encouraged to validate each module separately rather than integratively.

The limitations of past studies on closed-loop neural encoding/decoding were not adequately justified, weakening the contribution of the study.

The subtitles are not well match the items in the framework, making the manuscript is not easy to follow.

The encoding model has not been adequately validated. This module is very critical for the proposed framework. In addition, the implement details of the encoding model are not clear, e.g., was the model trained using individual data or data from multiple subject? How many training samples are used to train the encoding model? How to validate the model?

Is the EEG encoder which has been aligned with CLIP image features a good choice? This alignment may introduce bias in feature representation of the target and generated EEG signals. Why not a naive EEG encoder? 

All the figures and tables are not referenced in the main text, making it quite difficult to read the figures. For example, what is encoded by the dot size in Figure 3c? What is the image with red boundary in Fig. 3d step 10?

Are there any failure cases? What I can imagine includes: 1) the random samples in the first round roulette wheel fail to cover the target; 2) The generated images at a certain iteration fail to cover the target. The authors are encouraged to discuss this issue. 

“Since different stimulus images in our framework can produce the same or similar EEG features”—this could attribute to the existence of Metamers. However, other factors can not be overlooked: 1) the limitation of EEG (low spatial resolution) in quantifying brain activity. It might be possible that different stimulus image evoke similar EEG responses due to the limitations of EEG. 2) The limitation of the model for EEG feature prediction (the encoding model 3.1). The authors are encouraged to make justifications more carefully.

Other issues:
“quotation marks” are not in right format
The font size of some text in the figures are too small to read.
Typos: in Figure 4 captions: (F) is for O2 channel?

### Questions
1. The limitations of past studies on closed-loop neural encoding/decoding were not adequately justified, weakening the contribution of the study.
2. The subtitles are not well match the items in the framework, making the manuscript is not easy to follow.
3. The encoding model has not been adequately validated. This module is very critical for the proposed framework. In addition, the implement details of the encoding model are not clear, e.g., was the model trained using individual data or data from multiple subject? How many training samples are used to train the encoding model? How to validate the model?
4. Is the EEG encoder which has been aligned with CLIP image features a good choice? This alignment may introduce bias in feature representation of the target and generated EEG signals. Why not a naive EEG encoder? 
5. All the figures and tables are not referenced in the main text, making it quite difficult to read the figures. For example, what is encoded by the dot size in Figure 3c? What is the image with red boundary in Fig. 3d step 10?
4. Are there any failure cases? What I can imagine includes: 1) the random samples in the first round roulette wheel fail to cover the target; 2) The generated images at a certain iteration fail to cover the target. The authors are encouraged to discuss this issue. 
6. “Since different stimulus images in our framework can produce the same or similar EEG features”—this could attribute to the existence of Metamers. However, other factors can not be overlooked: 1) the limitation of EEG (low spatial resolution) in quantifying brain activity. It might be possible that different stimulus image evoke similar EEG responses due to the limitations of EEG. 2) The limitation of the model for EEG feature prediction (the encoding model 3.1). The authors are encouraged to make justifications more carefully.

Other issues:
“quotation marks” are not in right format
The font size of some text in the figures are too small to read.
Typos: in Figure 4 captions: (F) is for O2 channel?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper devised a closed-loop framework to find the visual stimuli that can elicit specific neural activities. The authors models the whole process as an MDP, and proposed to use the interactive search (mind matching) and heuristic search (genetic algorithm) to solve the problem. While claimed general, the authors specify the framework to  train the EEG encoding model to generate the synthesized EEG response and test it offline on the THINGS-EEG2 dataset. Visualized results demonstrate the possibility of the whole framework to find the appropriate visual stimuli in the search space. The authors also mentioned its possible impact and insights.

### Strengths
1. The whole framework is novel and interesting. It addresses the challenge to find the corresponding stimuli that can evoke a specific brain signal pattern. The framework may have the potential to be applied to a more realistic scenario. 
2. The paper proposed two different settings for finding the visual stimuli: retrieval and generation, and provided corresponding solutions for them. 
3. The overall findings may provide interesting neuroscience intuitions and may ignite further contributions.

### Weaknesses
1. One of the main claims by the authors is the adaptation of the whole close-loop framework. While the authors claim it can be simply replaced by recording EEG data from human participants, there are actually no more concrete demonstrations on how. For example, what is the "specific neural activity in the brain" in this paper and in a possible real scenario? What's the difference? And how difficult is it and how much effort will it take to apply the framework to the real world? It's always easy to just claim a methodology "generalizable", but without more justification that doesn't actually help strengthen the contribution of the paper. The authors should elaborate on the practical challenges of using real-time EEG data, such as signal noise, latency, and subject variability, and how these factors would impact the performance of their framework. A more detailed discussion of the required signal processing and calibration steps would also be beneficial.
2. Based on 1, I feel it is not sufficiently demonstrated in the paper what role the EEG plays in the whole framework. As far as I can understand from the current paper, it seems to be related to the reward $R$ in the MDP design, because it should provide signal based on the desired neural activities. However, we know neither how the reward is exactly calculated nor what kinds of the neural signal the authors are caring about (e.g., a specific frequency bank? a specific shape of waveforms? a specific activation from some brain area?). The paper lacks a clear definition of the EEG features used for reward calculation. It is unclear whether the authors are using raw EEG signals, preprocessed data, or features extracted from the EEG. The specific parameters of any preprocessing steps, such as filtering or artifact removal, should be specified. Furthermore, the rationale behind choosing specific EEG features over others should be discussed.
3. Besides the methodology, it's also not clear how the different part of this framework performs and contribute to the final result from the experimental aspect. While in the result section, we can see that the framework can yield promising visual stimuli result, it lacks either quantitative experiments and comparison between selection of algorithms, or a more detailed explanations on the presented ones. (See questions.) Therefore, it's unclear for me what the exact performance of the whole framework and individual parts compared to other solutions. The paper needs a more thorough evaluation of the framework's performance, including quantitative metrics and comparisons to baseline methods. The authors should also provide an ablation study to evaluate the contribution of each component of the framework. For example, what is the performance of the interactive search and heuristic search individually, and how do they compare to a random search? 
4. Overall, the presentation of this paper is unsatisfying (and that's probably why I have the concerns in 2 and 3). On the one hand, the author is presenting more well-known details in the main content but didn't make their own claims clear. For example, the algorithm 1 and algorithm 2 is a direct adaptation from previous work. Instead of using space to present them, I wish to see more on how the MDP is constructed. On the other hand, mixing citations with sentences (please use \citep instead \cite) and a few typos (in line 222, algorithm 1, the bracket is not matched) give me the feeling that the paper is not yet ready to be published.

### Questions
1. What kind of the neural activity are you concerning in your experiment? How will you verify whether the activity is properly stimulated by your visual stimuli?
2. If the answer to the previous question is via the EEG encoder, then how can the encoder capture your concerned neural activity? How does encoder perform? How will the selection of the encoder influence the result?
3. What is the reward in the MDP?
4. For Figure 3.B, why do you choose subject 8 for demonstration? It seems the confidence interval is large. I wonder whether the similarity increase can pass the significance test.
5. How to interpret the spectrograms in Figure 4.C? I can't see the difference or some trends from the figure. 
6. How is Figure 4.D obtained? Why does the "random" also look so good?

### Soundness
3

### Presentation
1

### Contribution
2
