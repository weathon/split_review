# SonicSim: A customizable simulation platform for speech processing in moving sound source scenarios

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
The systematic evaluation of speech separation and enhancement models under moving sound source conditions typically requires extensive data comprising diverse scenarios.
    However, real-world datasets often contain insufficient data to meet models' training and evaluation requirements. Although synthetic datasets offer a larger volume of data, their acoustic simulations lack realism. Consequently, neither real-world nor synthetic datasets effectively fulfill practical needs.
    To address these issues, we introduce \textit{SonicSim}, a synthetic toolkit designed to generate highly customizable data for moving sound sources. SonicSim is developed based on the embodied AI simulation platform, Habitat-sim, supporting multi-level adjustments, including scene-level, microphone-level, and source-level, thereby generating more diverse synthetic data. Leveraging SonicSim, we constructed a moving sound source benchmark dataset, \textit{SonicSet}, using LibriSpeech, Freesound Dataset 50k (FSD50K) and Free Music Archive (FMA), and 90 scenes from the Matterport3D to evaluate speech separation and enhancement models. 
    Additionally, to investigate the differences between synthetic and real-world data, we randomly selected 5 hours of raw data without reverberation from the SonicSet validation set to record a real-world speech separation dataset, which set a reference for comparing SonicSet and other synthetic datasets. Similarly, we utilized the real-world speech enhancement dataset RealMAN to validate the acoustic gap between the SonicSet dataset and other synthetic datasets for speech enhancement. The results indicate that models trained on SonicSet generalized better to real-world scenarios compared with other synthetic datasets. Demo and code are publicly available at \url{https://cslikai.cn/SonicSim/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a system and dataset for stimulating moving source sound data. The system is built using Habitat-sim which takes in a 3D scene and stimulates audio for receivers and transmitters placed at different locations. Simulated data for speech separation and speech enhancement problems are created, which are then used to benchmark performances of several state-of-the-art models for these problems. The results show that training models on simulated data can lead to better results on real-world dynamic audio.

### Strengths
– Simulating moving sound sources is indeed challenging and there are many good solutions for this problem. The paper relies on Habitat-sim and is a good attempt at improving simulation of moving sound sources. 

– From audio perspective, the proposed system provides a reasonable degree of freedom to simulate in various conditions.  

– The benchmarking of different speech separation and enhancement models is good – a variety of models for both tasks.

### Weaknesses
– The details of the moving source simulation could be improved a lot and is a major concern in the paper. Is the paper following  some known method ? Some mathematical description of what is going on in the moving source case is desirable, especially for description in Section 3.2.2 ? What exactly is SonicSim trajectory function “We then employed SonicSim’s trajectory function to calculate and generate a movement path for the sound source ” ? 

– Is the speed of the moving source a factor in the whole simulation process ? 

– Some ground truth validation of the simulations maybe helpful. For example, record data for a moving source in a real room and then use the 3D scene input of that room to simulate some data. How close are they ? 

– While the benchmarking on speech enhancement and separation are nice, a more useful benchmarking might be RIR estimation ? There are plenty of recent works on neural room acoustics generation and I think this problem would provide more insightful picture of the simulation system. 

– the paper mentions several challenges in audio simulations like obstacles, room geometry, room surface but none of them end up being a factor studied by the paper. 

– some aspects of the audio generation settings like the microphone type, monoaural vs binaural might be good to showcase.

### Questions
Please see the questions above.

### Soundness
2

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
SonicSim provides a new data simulator for moving sound sources for researchers working on speech separation and speech enhancement.  SonicSet is constructed using SonicSim using LibriSpeech, FreesoundDataset50k, and FreeMusicArchive, and 90 scenes from Matterport3D.

Using 9 speech separation models the authors show improvements when training on Voice-DEMAND, DNS Challenge, and SonicSet, and tested on the RealMAN test set, which shows significant improvement using SonicSet.

### Strengths
For researchers doing speech separation and enhancement with moving sound sources SonicSim and SonicSet will be valuable tools to create training data and training models. It fills an important gap in speech separation and enhancement dataset simulation.

### Weaknesses
SonicSim is constrained by the level of detail in 3D scene modeling.

For evaluation a subjective rating could have been used as done in DNS Challenge 2023 which would be more convincing than the objective metrics used (other than WER which is excellent).

SonicSim uses a MacBook Pro to play back speech, which is a poor choice to simulate a mouth. The directivity of a MacBook speaker is not representative of a human mouth. An artificial mouth, which mimics the frequency response and directionality of a human speaker, would be more appropriate.

Table 5: Says DNSMOS is used but it looks like SIGMOS used also? Please clarify which model MOS Sig, MOS BAK, and MOS Overall come from.

Table 6: Why are SI-SNR and WB-PESQ results much lower for Inter-SubNet than in the Inter-SubNet paper?

### Questions
What is the 5-hour dataset described in C.5 called (please give it a name - it is not SonicSet). Also why was a MacBook Pro used to play back speech? That seems like a very poor choice to simulate a mouth. Why not use an artificial mouth instead, which mimics the response of a human speaker (frequency response and directionality)?

How can new microphone types be added?

Table 5: Says DNSMOS is used but it looks like SIGMOS used also? Please clarify which model MOS Sig, MOS BAK, and MOS Overall come from. 

Table 6: Why are SI-SNR and WB-PESQ results much lower for Inter-SubNet than in the Inter-SubNet paper?

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
The paper introduces SonicSim, a customizable simulation platform designed to generate synthetic data for moving sound source scenarios, addressing limitations in real-world and existing synthetic datasets for speech separation and enhancement models. Built on Habitat-sim, SonicSim enables multi-level adjustments across scene, microphone, and source levels, providing flexibility for diverse scenarios. Using SonicSim, the authors created SonicSet, a benchmark dataset derived from Librispeech, FSD50K, FMA, and Matterport3D to evaluate models under moving sound conditions. Additionally, real-world data comparisons validate SonicSim's synthetic data, showing promising generalization to real-world scenarios.

### Strengths
The paper offers a toolkit for generating customizable synthetic data for speech processing in moving sound source scenarios, an area where realistic data is scarce. SonicSim stands out for its versatility in multi-level adjustments and the breadth of scenarios it enables. The SonicSet dataset, derived from a combination of diverse sources, is a method for benchmarking models in this field. The authors also make an effort to bridge the synthetic-real data gap by comparing SonicSet's synthetic data with real-world datasets, which enhances the reliability of SonicSim as a training and evaluation tool. Evaluations against evaluation metrics are pretty solid.

### Weaknesses
One potential limitation is the lack of human evaluation MOS metrics for quality measurement. Existing metrics like PESQ and DNSMOS are used, but the paper lacks inclusion of more advanced full-reference, as well as no-reference models like NISQA or SQAPP. These metrics could provide a statistically significant, nuanced understanding of synthetic data quality versus similarity to real-world audio, strengthening the claims around SonicSim's effectiveness.

### Questions
1. Have the authors considered implementing advanced full-reference, as well as no-reference MOS metrics such as NISQA or SQAPP, or even non-matching reference metrics? These could enhance the quality assessment of synthetic data and offer more insight into the real-synthetic data gap.

2. How well does SonicSim perform in dynamically noisy environments, where background sounds change over time? Would it be feasible to test in such conditions to increase practical applicability?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents SonicSim, a toolkit for generating realistic synthetic data in dynamic audio environments, specifically for moving sound sources. Built on Habitat-sim, this platform allows users to control variables like scene configurations, microphone types, and source movements. Using SonicSim, the authors created SonicSet, a new dataset to test models for speech separation and enhancement in several conditions. Results suggest that models trained on SonicSet perform better in real-world settings than those trained on other synthetic datasets.

### Strengths
1. SonicSim provides a customizable environment where users can adjust elements like scene layouts, source paths, and microphone setups.
2. SonicSim and SonicSet offer a promising step toward bridging the gap between synthetic and real-world audio data, which addresses current limitations in data for training speech front-end models.
3. The paper presents well-organized experiments, testing a variety of speech separation and enhancement models with a range of evaluation metrics like SI-SNR, SDR, and WER. These thorough experiments help demonstrate the value of SonicSet in preparing models for real-world conditions.
4. I appreciate the authors’ effort to make their work reproducible by providing open-source code and dataset.

### Weaknesses
1. I find the real-world testing too limited, as it relies heavily on the RealMAN dataset for speech enhancement (Section 5.5). Expanding testing to include other real-world data, perhaps by offering qualitative results on some in-the-wild examples (where speech is from actual conversations rather than recorded playback), would give a more comprehensive picture of how models trained on SonicSet generalize. That said, RealMAN alone may not be enough to fully support the claims of SonicSet’s real-world effectiveness, and an additional perceptual study would be highly beneficial.
2. Although the authors claim that SonicSim improves realism in reverberation modeling, there isn’t enough quantitative or qualitative support for this. I would recommend directly comparing SonicSim’s synthetic RIRs to real RIRs to demonstrate this realism. This type of comparison could show how much the enhanced realism of SonicSim truly benefits model performance.
3. While the paper covers a range of models for speech separation and enhancement, it’s unclear why these specific models were chosen. I think the authors should consider discussing a bit why one model is better than the other, and including more analysis to clarify how well SonicSim supports different model types.
4. SonicSet uses fixed LUFS levels for environmental and musical noise, which may limit how robust models are to different real-world noise levels. Adding tests with varied noise levels (like signal-to-noise ratios (SNRs)) could help demonstrate SonicSet’s ability to handle diverse noise conditions. I would also be interested to see how varying the noise characteristics affects model performance.
5. It’s not clear to me how flexible SonicSim is regarding scene layouts and material properties. It would help if the authors explained what can be adjusted versus what is fixed. This would allow readers to understand any limits in SonicSim’s adaptability.
6. Moving key details (training details, dataset splits, and evaluation metrics) into the main text would improve readability and reduce the need for readers to frequently switch sections, especially for understanding the experimental setup. The current Introduction section feels overly detailed and could be streamlined (reducing adverb use would improve clarity).

### Questions
See weaknesses. I'd be happy to increase my rating if the authors address the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
