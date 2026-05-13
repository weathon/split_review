

{0}------------------------------------------------

# --- Position: LLMs Are Too Cautious About Health, and It Is Hurting Vulnerable Users ---

Anonymous Author(s)

Affiliation

Address

email

## Abstract

1 Large language models (LLMs) are increasingly used as health information re-  
2 sources, yet their tendency toward over-cautious responses remains underex-  
3 plored. In this paper, we define over-cautiousness in LLM responses, examine its  
4 underlying causes, and discuss its negative consequences — particularly for vul-  
5 nerable populations such as individuals with OCD who are already prone to health  
6 anxiety. To systematically evaluate this phenomenon, we introduce OCD-Eval, a  
7 dataset of 225 queries centered on OCD-triggered health anxiety. Using both an  
8 LLM-as-judge approach and deterministic metrics, we measure the Over-Cautious  
9 Rate (OCR) by comparing risk levels assigned by General Practitioners (GPs) with  
10 those stated in model responses. Our evaluation of 22 LLMs reveals an average  
11 OCR of 43.9% on low-risk scenarios, demonstrating that over-cautiousness is a  
12 widespread and significant problem. We call for a recalibration of LLM values  
13 to enable models to accurately assess the true risk level underlying user queries,  
14 thereby reducing potential harm caused by unnecessarily alarming responses.

## 15 1 Introduction

16 Large Language Models (LLMs) are rapidly growing in capability and are now widely used as a  
17 routine source of information, particularly for specific and personalized questions. An Ipsos survey  
18 indicates that around 30% of U.S. consumers already turn to generative AI to address healthcare  
19 concerns between medical appointments (Choy et al., 2024). To mitigate the risk that LLMs provide  
20 harmful or unsafe guidance, developers typically align them to a set of safety preferences. However,  
21 these preferences are broad and developer-centric, and therefore do not fully reflect the wide range  
22 of real-world priorities and worries. In light of this alignment to safety preferences, we categorize  
23 LLM responses into three types: under-cautious, over-cautious, and appropriate. While the harms of  
24 under-cautious responses have received considerable attention in prior research, the potential dan-  
25 gers posed by over-cautious responses remain largely overlooked. While numerous studies examine  
26 LLM over-refusal, which can be interpreted as a form of over-cautiousness, they typically frame its  
27 drawbacks as reduced helpfulness (Cui et al., 2025; Röttger et al., 2024; Dabas et al., 2025) rather  
28 than as a safety concern in its own right. Among these, Zhang et al. (2026) is one of the few that rec-  
29 ognizes how over-refusal can drive users into misinformation sources, yet it does not address cases  
30 where LLMs do answer the question but with overly cautious framing. Formally, we characterize  
31 over-cautiousness in LLM responses by the following traits: 1. Objectively, the risk of an event is  
32 overstated. 2. Subjectively, the response creates a fearful or alarming tone.

33 To our knowledge, we are among the first to systematically investigate the harms associated with  
34 being overly cautious. We refer to this phenomenon as over-alignment, in analogy to overfitting in  
35 classical machine learning. In this paper, we argue that excessively cautious LLM responses to  
36 health-related queries can themselves be harmful, especially for vulnerable groups (Dorison

{1}------------------------------------------------

37 [et al., 2022](#); [Grant et al., 2022](#)) such as people with obsessive-compulsive disorder (OCD) and  
38 anxiety. We then illustrate the existence of this problem through a dataset.

![Figure 1: Overview of our position and dataset comparison. (a) A simplified illustration of our position in this paper. (b) A comparison of our seeddataset with original HealthBench.](9ba3dc91984c80b96f217fb1bddd5c06_img.jpg)

(a) A simplified illustration of our position in this paper. It shows two columns: 'Calibrated Response' and 'Overly Cautious Response'. Both columns show a 'USER QUERY' about a small cut on a leg, a 'MODEL RESPONSE' that is 'unlikely that you need a rubber plug', and an 'OUTCOME' that is 'Appropriate reassurance, reduced unnecessary worry, and better user experience'. The 'Overly Cautious Response' column shows a 'MODEL RESPONSE' that is 'You should consult a healthcare professional immediately' and an 'OUTCOME' that is 'Increased anxiety, unnecessary escalation, and worse user experience'. A note at the bottom states: 'Overly cautious responses, while well-intentioned, can lead to severe negative outcomes.'

(b) A comparison of our seeddataset with original HealthBench. It shows two columns: 'HealthBench' and 'Ours'. The 'HealthBench' column shows a 'USER QUERY' about mild chest pain, a 'MODEL RESPONSE' that is '49 WORDS | CONCERN', and an 'OUTCOME' that is 'NEUTRAL TONE'. The 'Ours' column shows a 'USER QUERY' about chest pain, a 'MODEL RESPONSE' that is '49 WORDS | CONCERN', and an 'OUTCOME' that is 'RECURRING + RE-HISTORY' and 'ANXIOUS, CONFUSED'. A note at the bottom states: 'Our dataset captures realistic, emotionally-loaded queries that general benchmarks miss.'

Figure 1: Overview of our position and dataset comparison. (a) A simplified illustration of our position in this paper. (b) A comparison of our seeddataset with original HealthBench.

(a) A simplified illustration of our position in this paper.

(b) A comparison of our seeddataset with original HealthBench

Figure 1: Overview of our position and dataset comparison.

###### 39 2 Related Works

###### 40 2.1 Concerns over LLM Alignment

41 There are many concerns over LLM or AI (pre-LLM era) alignment. We focus on two concerns  
42 that are closely connected to our topic here. First, how should LLMs construct their value systems?  
43 Second, are LLMs capable of handling the diversity of real-world contexts, such as cultural and  
44 situational variation?

45 Regarding the question of how LLMs should construct their value systems, AI developers often  
46 claim that they have aligned their AI with “human values” or “human preferences”, to increase its  
47 usefulness and harmlessness, including InstructGPT and Anthropic AI ([Ouyang et al., 2022](#); [Bai](#)  
48 [et al., 2022](#); [Hendrycks et al., 2023](#)). [Sutrop \(2020\)](#) concerns that AI developers underestimated  
49 the difficulty of the question about which values or whose values the AI should align with. The  
50 authors argued that given that our everyday life is full of moral disagreements and the plural na-  
51 ture of values, how can we decide which objectives or values we inject into the AIs? [Arzberger](#)  
52 [et al. \(2024\)](#) argues that current alignment approaches rely on universal framings of human values,  
53 framings that are not inherently neutral or impartial, and that this can be problematic, leading to  
54 AI systems that are biased and to equity and justice issues. Given this inherent bias in AI systems,  
55 current LLMs tend to struggle with nuanced queries that involve cross-cultural diversity or situa-  
56 tional complexity. For example, [Segerer \(2025\)](#) finds that DeepSeek (a Chinese LLM) shows more  
57 value towards collectivism compared to Western LLMs. [Münker \(2025\)](#) states that their study sug-  
58 gests a concerning reality: “Large Language Models (LLMs) fail to represent diverse cultural moral  
59 frameworks despite their linguistic capabilities.” They highlighted the need for culturally-informed  
60 alignment objectives. Current approach regresses the model to a “mean moral framework” rather  
61 than representing diverse human values. Without cross-cultural evaluation metrics, models may ap-  
62 pear well-aligned within the tested context but fail to perform appropriately under alternative moral  
63 frameworks. Besides cultural complexity, another side of the same coin, more related to LLMs’  
64 health responses, is situational complexity. This is a well-studied area of AI over-refusal, where AI  
65 refuses to answer a question, in the name of safety, to some queries that are benign in the specific  
66 context. Common examples include how to make a TNT in Minecraft or how to kill a child process  
67 ([Zhang et al., 2025](#)). [Ray & Bhalani \(2024\)](#) also studied LLMs’ over-refusal in cases like prompts  
68 with homonyms (e.g., how to kill a process) or safe context (“how to kill someone in [a video game  
69 name]”), etc. They found that many LLMs have problems with over-refusing prompts.

{2}------------------------------------------------

###### 70 2.2 LLM and Risk Handling

71 A large body of literature examines LLMs’ approach to risk, with findings suggesting that over-  
72 cautiousness in LLMs can have negative consequences across a wide range of domains. For instance,  
73 Ouyang et al. (2025) studied how LLMs’ cautiousness in ethical alignment affects economically  
74 valuable risk-taking, which might affect economic forecasts and suppress valuable risk-taking. Cui  
75 et al. (2025) is another benchmark and evaluation for model over-refusal, and they found a positive  
76 relationship between over-refusal and safety.

###### 77 2.3 HealthBench

78 A closely related effort is OpenAI’s HealthBench (Arora et al., 2025), which includes an  
79 emergency-referral:non-emergent category aimed at assessing whether models recommend  
80 escalation when it is not warranted, alongside genuine emergency scenarios. This category  
81 was introduced in light of the concern that excessive triage could “strain already overburdened health  
82 systems,” and the dataset was both constructed and validated by healthcare professionals. In practice,  
83 this setup also probes whether models systematically favor overly cautious recommendations:  
84 a model that repeatedly escalates without need can be viewed as over-cautious.

85 However, HealthBench is chiefly focused on the accuracy and appropriateness of answers to general  
86 medical queries. In contrast, our work contends that excessive caution can directly harm individual  
87 users *themselves*, especially those with OCD or anxiety disorders. We assess model outputs  
88 not only for correctness, but also for whether they reinforce maladaptive OCD thought patterns.  
89 Moreover, HealthBench’s over-caution assessment is largely limited to decisions about whether a  
90 patient should immediately seek emergency care, which covers only a narrow slice of the broader  
91 OCD-related anxiety landscape. Additionally, the prompts in our evaluation mirror the style and  
92 content of questions typically asked by individuals with OCD and anxiety, rather than general health  
93 inquiries as in HealthBench. A chest pain comparison example is provided in Figure ??.

###### 94 2.4 Health Tools, OCD, and Anxiety

95 Vulnerable users, particularly those with health anxiety or OCD, face unique risks when using health  
96 information tools. Prior to the widespread adoption of LLMs, such individuals were already turning  
97 to resources such as online symptom checkers and nursing helplines for medical reassurance. One  
98 study (Wetzel et al., 2024) found that health anxiety (used to be named hypochondria) is a reliable  
99 predictor of symptom checker application (SCA) use, and Mohammed et al. (2019) found over one  
100 third of people who conduct internet health searches exhibit signs of Cyberchondria. Critically, users  
101 with significant health anxiety may be particularly vulnerable to the adverse effects of these tools:  
102 Doherty-Torstrick et al. (2016) found that people with high health anxiety feel more anxious after  
103 online symptom checking, while the low health anxiety population feels more relief after online  
104 symptom checking.

105 With the rise of LLMs, these risks may be amplified. Aslam & Nisar (2023) warned that as LLMs re-  
106 spond in human-like text, more people may turn to them for health information, potentially increas-  
107 ing the prevalence of Cyberchondria. Moreover, repeated exposure to disease names and symptoms  
108 through LLM interactions may produce effects analogous to “Medical student syndrome,” where  
109 “Medical students are at higher risk for health anxiety and hypochondriacal attitudes than non-  
110 medical students are (Sherif et al., 2023).” In this sense, LLM interactions may expose users to  
111 a similar dynamic, even in the absence of formal medical training. These findings underscore the  
112 importance of ensuring that LLM responses do not inadvertently exacerbate anxiety in vulnerable  
113 users.

114 Wong et al. (2025) highlighted that even factually correct outputs can be highly misleading, further  
115 exacerbating user anxiety. For instance, the AI might reference a study claiming that something *sig-*  
116 *nificantly* increases the risk of a condition. While this is technically accurate, the term “significantly”  
117 has different meanings in scientific literature versus everyday language: in the former it typically  
118 refers to statistical significance, whereas in the latter it implies a substantial absolute change. Sim-  
119 ilar problems arise when the model gives different answers depending on how the user phrases the  
120 question (for example, “why it is safe” versus “why it is risky”). In such situations, the LLM shows  
121 strong information retrieval and synthesis capabilities but lacks appropriate communication skills  
122 to present information in a clear, consistent way that avoids being misleading. Our anecdotal ob-

{3}------------------------------------------------

123 servations also agree with this suggesting that LLMs often highlight specific studies that support a  
124 given conclusion, treating peer-reviewed papers as absolute gold standard, while overlooking other  
125 sources of disagreement and the nuances within the research. Two examples are listed in Appendix.

###### 126 3 Position

127 Our position challenges the premise that models should be aligned to “human values/preferences”  
128 in an absolute sense, for health queries, particularly when this concept is oversimplified in health  
129 contexts as “always erring on the safe side.” While AI safety discourse typically focuses on prevent-  
130 ing risky behavior, we highlight the opposite danger: overly cautious responses that can exacerbate  
131 conditions like anxiety and OCD by reinforcing harmful behavioral patterns. We form our argument  
132 in two layers: why LLMs are prone to over-caution and why this is harmful.

133 LLMs are prone to over-caution for two interconnected reasons. Firstly, LLMs responses are always  
134 grounded in alignment with human values, yet the concept of universal “human values/preferences”  
135 is inherently problematic due to value pluralism and context dependency (Segerer, 2025; Arzberger  
136 et al., 2024; Münker, 2025). As Arzberger et al. (2024) notes, current alignment methods rely on  
137 supposedly universal values that may be biased against certain populations. As a result, LLMs tend  
138 to lack contextual awareness and default to uniformly conservative responses across all users — for  
139 example, advising everyone to “see a doctor if you’re worried” regardless of the actual risk level  
140 involved. While this may be entirely reasonable for typical users facing genuine health concerns,  
141 for individuals who already harbor pronounced anxiety about highly unlikely risks, such responses  
142 are anything but helpful: they may not only intensify existing worries, but also quietly reinforce  
143 maladaptive patterns of thinking. It also encourages more frequent doctor visits, which may increase  
144 secondary risks and place unnecessary burdens on time and resources for both the patient and the  
145 public health system. Secondly, LLM developers, similar to the online symptom checker developers,  
146 are facing significant legal and public relations pressures. The fear of being sued or facing liabilities  
147 is one of the real drivers that developers are tuning their tools to be conservative; this is a common  
148 effect in almost any industry as a defensive practice (e.g., you may always see a “Wet Floor” sign in  
149 many places even if the floor is dry or you see P65 warning in many places even if they do not pose  
150 a danger). Under such pressures, excessive caution becomes an almost inevitable default.

151 When taken to extremes, aligning AI with human values around safety — that is, *always* erring on  
152 the side of over-caution — can itself become harmful. Turchin (2019) argued that human values can-  
153 not be scaled and that some values serve to balance others. Maximizing certain values in isolation,  
154 without their counterparts, can be dangerous. This idea aligns with the virtue theory of the ancient  
155 Greeks, which holds that people should cultivate good character and that both excess and deficiency  
156 of certain traits are detrimental. The same principle applies to AI design. In our specific examples,  
157 an over-aligned AI that maximizes “safety” and “do no harm” may in fact cause harm because it  
158 fails to balance those goals with other human values such as reasonableness and rationality, which  
159 developers might overlook.

160 The harms resulting from over-alignment are not only mental but also physical. Over-cautious re-  
161 sponses intensify users’ anxiety, and the chronic stress that follows can in turn take a tangible toll on  
162 physical health as it is a well-established medical fact that stress and anxiety has a direct impact on  
163 physical health. Excessive cleaning or the use of inappropriately strong methods can lead to skin or  
164 mucosa damage and infections. Avoidance behaviors, such as avoiding clinics due to contamination  
165 anxiety, can delay necessary medical visits. Conversely, over-visiting doctors increases infection  
166 risk. Unnecessary medical tests can cause direct harm and undermine trust, affecting future health  
167 decisions. Fear-driven avoidance of certain foods can lead to an unbalanced diet. LLMs likely will  
168 not directly suggest these behaviors; however, the reinforced anxiety might lead users to them as a  
169 form of secondary harm. In extreme cases, some studies show that OCD has been linked to death  
170 from suicide and accidents (Mayo Clinic; Meier et al., 2016; Fernández de la Cruz et al., 2022, 2017;  
171 Ferreira et al., 2018), although some research shows otherwise. Either this imbalance of values is  
172 intentional, stemming from the designer, or it is an unintentional bias in the dataset; in either case,  
173 it shows that scaling and generalizing certain values around safety can result in harm.

174 These harms are also intensified for particularly vulnerable groups within the OCD population:  
175 people living in remote areas, in regions with lower medical standards, and individuals with low  
176 income. For those in remote locations and with limited financial resources, seeking unnecessary

{4}------------------------------------------------

177 medical care demands significantly more time, money, opportunity cost, or consequences (e.g., job  
178 loss or social stigma). In areas where healthcare quality is lower, pursuing unnecessary treatment  
179 may also expose them to misinformation or unverified interventions. Moreover, these individuals are  
180 less likely to have access to mental health professionals who can identify their reassurance-seeking  
181 behavior as a symptom of OCD, meaning they may not realize that their actions are reinforcing their  
182 anxiety rather than alleviating it.

###### 183 4 OCD-Eval

184 In the previous section, we argued that overly cautious responses can be harmful. In this section, we  
185 will examine whether this problem occurs in LLMs and, if so, how severe it is.

186 As discussed in the related work section, although HealthBench includes queries related to over-  
187 cautious behavior, those questions simulate general user interactions with legitimate health concerns.  
188 While one could rewrite them to incorporate OCD-related tone and thought patterns, we found  
189 that the resulting queries often became awkward or implausibly anxious given their trivial medical  
190 context (e.g., a user asking whether a bug bite requires an ER visit), making them easy for LLMs  
191 to give simple rule based correct answer (not escalating) rather than genuinely testing for over-  
192 alignment. Given this limitation, we constructed a focused evaluation set of 225 queries centered on  
193 OCD-triggered health anxiety. The size exceed the non-emergency category of HealthBench (134).  
194 These queries are narrowed down using both embedding-based and keyword searches, and then  
195 each one is rigorously checked individually by a human validator. The questions were sourced from  
196 two authors with past or current OCD experiences. We filtered out questions that are too obvious  
197 (too low risk) such as worries about 405mg caffeine intake (limit is usually 400mg) and infection of  
198 smallpox. A word cloud of our dataset is shown in Figure 3 in Appendix. For a trade-off comparison  
199 and sanity check, we also evaluate how well the models can recognize real medical emergencies by  
200 using the emergency subset from HealthBench.

201 We began by evaluating the models with reasoning disabled, since this is the mode most users  
202 use when chatting with LLMs. We then enabled reasoning for the three most recent reasoning  
203 models (GPT-5.5, Gemini-3-Flash, and Claude-Sonnet-4.6) to see whether it affected their level of  
204 cautiousness.

205 All questions are assessed by General Practitioners (GPs) recruited via Prolific. For each question,  
206 a GP evaluates the level of risk in the scenario. The GP is given the OCD context of patient for  
207 labelling. We did not use GP's answer of whether an LLM's response shows appropriate risk  
208 calibration for both the general population and individuals with OCD, because we consider it difficult  
209 for GP to judge what is suitable for someone with an OCD background, and their thresholds vary as  
210 well.

211 In total, 7 GPs annotated the dataset, with each question-AI answer pair labeled by a single GP.  
212 The label distribution is: no risk 60.3%, minor risk 30.9%, medium risk 5.3%, and high risk 3.3%.  
213 Since our analysis focuses on non-high-risk scenarios where over-cautiousness can be meaningfully  
214 evaluated, we removed questions labeled as high risk. To validate the reliability of this filtering, we  
215 selected 50 questions from the remaining set and had them re-labeled by a separate group of five GPs  
216 (excluding previous Prolific participants). We calculated the agreement on these questions and get a  
217 exact agreement of 0.70, quadratic weighted Gwet's AC2 of 0.93, and linear weighted AC2 of 0.83,  
218 MAE of 0.3 and signed AE of 0.02, showing very high agreement, indicating that two GPs labeling  
219 the same question arrived at highly consistent results. We verified that none of the second-round  
220 annotations reclassified any retained question as high risk. We also computed the fraction of cases  
221 in which the second relabel risk exceeded the first label, which is 0.16. Accounting for the inherent  
222 randomness in annotation, this value can be interpreted as an upper bound on the probability that  
223 random disagreement affects the "over-cautious" metrics. In other words, if a model's over-cautious  
224 rate (OCR) exceeds 0.16, its over-cautiousness is unlikely to be attributable to random annotation  
225 noise, but rather reflects a genuine tendency toward over-caution in the model itself.

###### 226 4.1 Metrics

227 We employed both an LLM-as-judge approach, using Deepseek V4 Pro (DeepSeek-AI, 2026) from  
228 OpenRouter, and deterministic metrics. Using the LLM-as-judge setup, we primarily evaluated

{5}------------------------------------------------

229 whether the model’s responses matched six predefined answer patterns, as listed in Table 1 in Ap-  
230 pendix. Because this evaluation reduces to straightforward pattern matching, we can reliably use the  
231 LLM judge for this purpose.

232 In addition, we require the evaluated LLM (not the judging model) to append a final risk rating at  
233 the end of its answer, using the same risk categories as the GP, and explicitly output this final risk  
234 level at the conclusion of its response. We compute two metrics: the over cautious rate (OCR) and  
235 the significant over cautious rate (SOCR). OCR measures how often the model’s predicted final risk  
236 exceeds the ground truth, while SOCR captures cases where the model’s predicted risk is two levels  
237 or higher than the ground truth. We divided the dataset into two categories. The first, called low  
238 risk, contains questions that the GP labeled as negligible risk. Many of these are trivial, such as a  
239 user asking whether they should worry about walking on yellow road paint on the ground because  
240 of potential lead exposure. The second category, medium risk, contains questions involving real  
241 risks, where we want to see whether the model will respond in an alarmist way to those risks.  
242 Our primary focus is on the OCR, because we want to know whether the AI assigns any risk level  
243 above negligible. Even labeling the risk as “low” (and not “negligible”) for OCD patients can cause  
244 worrying to the user, as they may feel that “low” is still not “low enough.” This is likely due to  
245 intolerance of uncertainty, perfectionism, and overestimation of threat.

###### 246 4.2 Results

247 The primary results are presented in Figure 2 and Table 2 in Appendix shows the full results of  
248 the model’s OCR and SOCR on both low and medium risk cases. Most models performed reason-  
249 ably well on emergency recognition (> 90%). However, many exhibited severe over-cautiousness,  
250 particularly earlier or smaller models. We also compared our emergency recognition results with  
251 the original HealthBench report Arora et al. (2025). Our scores are slightly higher but remain in  
252 a similar range; for instance, GPT-4.1 achieved 0.92 on the original HealthBench and 0.95 on our  
253 evaluation. This discrepancy is likely attributable to differences in evaluation procedures and model  
254 stochasticity. Latest models are showing around 20-30% of OCR, while some models shows over  
255 50% over cautious rate. Surprisingly, the model shows higher OCR scores under low-risk settings,  
256 while SOCR scores are low for both low-risk and high-risk settings. This indicates that the AI is  
257 unlikely to greatly exaggerate the risk, but will still tend to elevate the stated level of risk, especially  
258 when the real risk is negligible, the AI still tends to describe it having low risk. As noted, this could  
259 still heighten anxiety in individuals with OCD because of their characteristic thought patterns.

260 The tag frequencies are reported in Table 4 in Appendix. Note that each response could receive  
261 multiple tags. Several patterns emerge that may heighten users’ anxiety. In particular, symptom  
262 checking stands out. All models indicated a high level of symptom checking. While not all instances  
263 of symptom checking are problematic, in no- or low-risk situations, telling the user to “keep an eye  
264 on” symptoms simultaneously communicates that something *might* go wrong and that it requires  
265 their attention, which may contribute to a nocebo effect. Another notable pattern is reassurance  
266 undermining, where the model acknowledges that the risk is low but then hedges and lists potential  
267 dangers. Individuals with OCD are likely to fixate on the mention of these risks rather than on the  
268 statement that the risk is low.

269 Importantly, most models rarely provide mental health support in their responses (Provide Anxiety  
270 Help rate under 50% across models, see Table 4). This raises a clinical dilemma: providing direct  
271 reassurance (e.g., “this is very low risk”) offers temporary relief but may reinforce the reassurance-  
272 seeking cycle central to OCD and health anxiety. However, we argue that reassurance is still prefer-  
273 able to alarming responses. An alarming response spikes the user’s immediate anxiety and drives  
274 them toward compulsive actions such as visiting the emergency room — and in doing so, it im-  
275 plicitly offers its own form of reassurance: the anxiety is temporarily resolved once the compulsive  
276 action is completed. In effect, the model replaces one reassurance-seeking loop with another that  
277 carries greater cost and distress. The optimal response, therefore, is to briefly acknowledge the  
278 low risk without excessive elaboration, while suggesting that the recurring pattern of worry itself  
279 may benefit from professional mental health support. We also included example responses in the  
280 Appendix.

{6}------------------------------------------------

###### 281 4.3 When Model is Given Patient’s OCD Context

282 We selected the six most recent models, provided each with the user’s OCD and health-anxiety  
283 background, and instructed them to avoid triggering that anxiety. The results suggest that this is  
284 not a reliable solution. Adding this context substantially reduced many models’ ability to identify  
285 emergencies (Gemma 3 27B recognized only 68.0% of true emergencies), while over-cautiousness  
286 was not consistently reduced (GPT 5.5 Thinking still labeled negligible-risk situations as low risk  
287 44.2% of the time). For several models, this approach produced the worst of both outcomes —  
288 degraded emergency recognition without meaningful reduction in over-cautiousness. While Gemini  
289 3 Flash and its Thinking variant performed better, this represents only two out of six models, and  
290 the inconsistency across models makes this approach unreliable as a general solution. Furthermore,  
291 most users with OCD are undiagnosed and cannot self-identify their condition, and disclosing men-  
292 tal health information to an LLM raises significant privacy concerns. This reinforces our central  
293 argument: the solution must lie in recalibrating models themselves, rather than placing the burden  
294 on users to disclose their condition.

###### 295 5 Potential Solutions

296 **Industrial Standards and Metrics.** Datasets such as HealthBench and our Mini-OCD-Eval can  
297 serve as foundations for developing industry standards. A key component of this process is the in-  
298 volvement of healthcare professionals — not primarily to judge whether model responses are over-  
299 cautious, but to provide ground-truth risk assessments for health-related scenarios. These annota-  
300 tions establish an objective baseline that makes it possible to define what constitutes an appropriate  
301 response, and to measure and compare model behavior across systems. Building on this foundation,  
302 independent third-party organizations working with healthcare professionals can establish clear cri-  
303 teria specifying when health-related queries should be escalated and when they should not, as well  
304 as how to appropriately support vulnerable users, including those with OCD and anxiety. Such over-  
305 sight would encourage LLM developers to make their systems more accountable and user-oriented,  
306 rather than focused on overly defensive practices.

307 **More Professionals in Alignment.** We can include more health professionals in the alignment,  
308 designing specific training datasets, and when evaluating, focus on both over- and under-cautious.  
309 HealthBench (Arora et al., 2025) has already addressed that emergency triage mistakes, both over-  
310 and underdiagnosis, could be harmful, and future alignment efforts should extend this principle to  
311 non-emergency, anxiety-related scenarios as well.

312 **User and Public Education.** For individuals who have OCD but have not been diagnosed, it is cru-  
313 cial to encourage them to seek professional mental health care. This can be supported through better  
314 education about OCD and the risks of health anxiety, provided either through public resources like  
315 OCD Awareness Week or by LLMs when a representative pattern appears in a user’s conversation  
316 — for instance, when repeated low-risk health queries suggest anxiety-driven reassurance-seeking  
317 rather than genuine medical concern. Meanwhile, the general population, including people with  
318 and without OCD, should also be aware that current LLMs tend to be overly cautious and are not  
319 well calibrated to actual levels of risk. Healthcare workers should additionally be more attentive to  
320 signs of health anxiety or OCD in order to refer patients to appropriate mental health or psychiatric  
321 services when these symptoms appear, doing so in a non-judgmental manner rather than dismissing  
322 their concerns with brief reassurance (Sullivan, 2025).

###### 323 6 Alternative Positions

324 Our central thesis is that “some LLMs suffer from over-alignment, and this is hurting vulnerable  
325 populations such as OCD and anxiety patients.” We considered a couple of alternative positions  
326 (counterarguments) and rebutted them as follows.

327 **“Over-cautious behavior minimizes harm at scale, while under-cautious responses carry**  
328 **greater consequences.”** The objection that under-cautious responses to genuine emergencies can be  
329 immediately fatal while over-cautious responses cause only incremental psychological harm appears  
330 compelling, but our empirical results suggest otherwise. As shown in Table 2, over-cautiousness  
331 varies substantially across models, yet Emergency Recognition remains consistently high across the

{7}------------------------------------------------

![](c3c305cefbac2e7b13be34ab87054d1e_img.jpg)

Figure 2: Main results on how accurately the model detects real emergencies in HealthBench, and the how overly cautious models are on our OCD-Eval.

332 board (96.1% overall). Critically, models with the lowest OCR scores do not show worse Emer-  
333 gency Recognition: for instance, claude-sonnet-4.6 achieves an OCR(Low) of only around 20%  
334 while maintaining an Emergency Recognition of around 98%, whereas gemini-3-flash, which has  
335 a similar Emergency Recognition rate but over cautious 30% of the time, a 50% increase. This  
336 pattern suggests that reducing over-cautiousness and maintaining emergency recognition are not in  
337 tension — both can be achieved simultaneously. The assumption that improving calibration neces-  
338 sarily comes at the cost of emergency safety is therefore not supported by the data: the trade-off  
339 this objection presupposes does not appear to be zero-sum. In fact, within the same model fam-  
340 ily, many versions achieve both higher emergency recognition and a low rate of over-cautious re-  
341 sponses, even though this pattern is not consistently maintained over time. Comparing Gemma 3 to  
342 Gemma 4, Gemini 2.0 Flash to Gemini 3 Flash, and Claude 3.7 Sonnet to Claude Sonnet 4.6, they  
343 all move toward the top-left corner of the figure, likely due to better general abilities and knowledge.  
344 While some outliers and regressions exist, the existence of models that simultaneously achieve high  
345 emergency recognition and low over-caution demonstrates that good calibration is an achievable  
346 engineering goal, not a fundamental trade-off.

347 This argument also prioritizes the general population's safety over the well-being of vulnerable  
348 individuals, treating the psychological burden imposed on them as an "acceptable cost" for the  
349 collective good. This approach is unfair to those who are vulnerable. This not only downplays the  
350 psychological distress of vulnerable individuals, which in many cases has equal or greater effects  
351 on one's livelihood, but it also ignores the physical harm, and potentially also catastrophic, that could  
352 occur from the over-cautious behaviors (See first point of position section). Additionally, based  
353 on previous research (Wetzel et al., 2024; Mohammed et al., 2019), a significant amount of people  
354 researching health-related questions online are already experiencing health anxiety (between 30%  
355 and 50%). Assuming a similar ratio in the landscape of LLMs, even though health anxiety and OCD  
356 are relatively rare in the general population, LLMs' over-cautious response might have a significant  
357 impact on these people.

358 **“People with anxiety and OCD should not use LLMs as a tool for reassurance.”** This is technically  
359 correct, and we do not dispute it as a therapeutic principle. However, this principle addresses  
360 the behavior of patients, not the design of LLM responses. The question we are concerned with is  
361 different: given that users do seek reassurance from LLMs — whether due to limited self-awareness,  
362 lack of access to therapy, or the gradual nature of behavioral change — what kind of response causes  
363 the least harm becomes the central question. This counterargument, as a principle of OCD treatment,  
364 actually contains two distinct claims: (1) OCD patients should not frequently seek health advice  
365 from LLMs; and (2) LLMs should not provide reassurance to OCD patients regarding their queries.  
366 We address each claim in turn.

367 Regarding the first claim, whether OCD patients choose to consult LLMs is not directly relevant

{8}------------------------------------------------

368 to the central argument of this paper. Our focus is on whether over-cautiousness exists in LLM  
369 responses and the negative consequences it produces for users. The first claim concerns constraints  
370 on the behavior of OCD patients themselves, while the latter concerns the quality of LLM responses  
371 — these are distinct issues and should not be conflated.

372 Regarding the second claim, as discussed in Section 4.2, the key question is not whether to provide  
373 reassurance, but which form causes less harm. We acknowledge that from a strict ERP perspective,  
374 even a well-calibrated reassurance may reinforce reassurance-seeking behavior. However, this  
375 observation does not bear on the recommendation we are making. Our argument is not that well-  
376 calibrated responses are therapeutically optimal for OCD patients in an absolute sense — it is that  
377 they are less harmful than over-cautious responses for low-risk queries. Once a user has already sub-  
378 mitted a query, the reassurance-seeking interaction has already occurred. An over-cautious response  
379 does not avoid the reassurance loop — it redirects it toward more costly compulsive actions such  
380 as emergency room visits. A well-calibrated response, by contrast, contains the same reassurance-  
381 seeking episode without the additional burden of unnecessary anxiety and compulsive behavior.  
382 The goal of this paper is therefore a targeted improvement within a constrained situation: reducing  
383 the marginal harm introduced by over-cautiousness, not resolving the broader clinical challenge of  
384 reassurance-seeking itself.

385 In sum, when the interaction of "a user seeking advice from an LLM" has already occurred, the  
386 appropriate goal is to avoid over-cautiousness, which imposes unnecessary additional psychological  
387 burden on the user.

388 **"Traditional health tools have the same problem, why LLMs should be different"** Firstly, traditional  
389 tools doing so does not mean it is the correct approach. Traditional health tools faced similar  
390 criticism, as shown in the related work section. This is not an excuse for LLMs to do the same. Ad-  
391 ditionally, LLMs should have better contextual understanding and nuance than traditional rule-based  
392 tools due to their better reasoning capability and flexible interface.

393 **"Models are not good at medical knowledge, and thus it is better to be more careful"** It was once  
394 accurate to say that an LLM was merely a chatbot capable of producing fluent text while lacking  
395 genuine world or domain-specific knowledge. That characterization, however, is now outdated. Re-  
396 sults from HealthBench (Arora et al., 2025) and MedXpertQA Zuo et al. (2025) show that late-2024  
397 models can already surpass physicians or pre-licensed experts when answering without external ref-  
398 erences, indicating that current systems have knowledge and expertise on par with clinical profes-  
399 sionals. By early 2026, models such as Qwen3.5-122B-A10B—and even smaller, edge-deployable  
400 models like Qwen3.5-35B-A3B—have achieved scores above 0.6 on MedXpertQA, compared with  
401 a pre-licensed expert baseline of about 0.44. Other SOTA models, while not reported their scores,  
402 likely have similar level of medical knowledge. Nonetheless, they still exhibit pronounced over-  
403 cautiousness. We therefore argue that this overly conservative behavior arises not from protection  
404 against knowledge deficits, but from alignment-induced artifacts. Although on HealthBench emer-  
405 gency subset models still do not achieve a 100% emergency recognition rate, we can observe that  
406 the models are progressing toward reduced over-cautiousness and improved emergency recognition.  
407 This indicates we are moving in the right direction and that reaching this goal should be feasible in  
408 the future.

###### 409 7 Conclusion

410 This paper demonstrates that LLM over-cautiousness is a widespread, measurable problem, with an  
411 average 43.9% over-cautious rate on low-risk health scenarios, and that it poses real harm to vulner-  
412 able populations like those with OCD and health anxiety. The empirical results show that reducing  
413 over-cautiousness and maintaining high emergency recognition are not in tension, as several models  
414 achieve both simultaneously. Recalibrating LLM alignment to reflect actual risk levels, rather than  
415 defaulting to maximum caution, is both feasible and necessary to avoid turning a safety mechanism  
416 into a source of harm.

{9}------------------------------------------------

## 417 References

- 418 Rahul K. Arora, Jason Wei, Rebecca Soskin Hicks, Preston Bowman, Joaquin Quiñonero-Candela,  
419 Foivos Tsimpourlas, Michael Sharman, Meghan Shah, Andrea Vallone, Alex Beutel, Johannes  
420 Heidecke, and Karan Singhal. HealthBench: Evaluating Large Language Models Towards  
421 Improved Human Health, May 2025. URL <http://arxiv.org/abs/2505.08775>.  
422 arXiv:2505.08775.
- 423 Anne Arzberger, Stefan Buijsman, Maria Luce Lupetti, Alessandro Bozzon, and Jie Yang. Nothing  
424 Comes Without Its World – Practical Challenges of Aligning LLMs to Situated Human Values  
425 through RLHF. *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*, 7:61–73,  
426 October 2024. ISSN 3065-8365. doi: 10.1609/aies.v7i1.31617. URL <https://ojs.aaai.org/index.php/AIES/article/view/31617>.  
427
- 428 Muhammad Shahzad Aslam and Saima Nisar. *Artificial Intelligence Applications Using ChatGPT in*  
429 *Education: Case Studies and Practices*. Advances in Educational Technologies and Instructional  
430 Design. IGI Global, September 2023. ISBN 9781668493007 9781668493014. doi: 10.4018/  
431 978-1-6684-9300-7. URL [https://services.igi-global.com/resolvedoi/](https://services.igi-global.com/resolvedoi/resolve.aspx?doi=10.4018/978-1-6684-9300-7)  
432 [resolve.aspx?doi=10.4018/978-1-6684-9300-7](https://services.igi-global.com/resolvedoi/resolve.aspx?doi=10.4018/978-1-6684-9300-7).
- 433 Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn  
434 Drain, Stanislas Fort, Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath, Jackson  
435 Kernion, Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac Hatfield-Dodds, Danny Hernandez,  
436 Tristan Hume, Scott Johnston, Shauna Kravec, Liane Lovitt, Neel Nanda, Catherine Olsson, Dario  
437 Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann, and Jared Kaplan.  
438 Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback,  
439 April 2022. URL <http://arxiv.org/abs/2204.05862>. arXiv:2204.05862.
- 440 Vanessa Choy, Sara Martin, and Ashley Lumpkin. Can we rely on generative AI  
441 for healthcare information?, 2024. URL [https://www.ipsos.com/en-us/](https://www.ipsos.com/en-us/can-we-rely-generative-ai-healthcare-information)  
442 [can-we-rely-generative-ai-healthcare-information](https://www.ipsos.com/en-us/can-we-rely-generative-ai-healthcare-information). publisher: Ipsos.
- 443 Justin Cui, Wei-Lin Chiang, Ion Stoica, and Cho-Jui Hsieh. OR-Bench: An Over-Refusal Bench-  
444 mark for Large Language Models, June 2025. URL [http://arxiv.org/abs/2405.](http://arxiv.org/abs/2405.20947)  
445 [20947](http://arxiv.org/abs/2405.20947). arXiv:2405.20947.
- 446 Mahavir Dabas, Si Chen, Charles Fleming, Ming Jin, and Ruoxi Jia. Just Enough Shifts: Mitigat-  
447 ing Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning. June  
448 2025. URL <https://openreview.net/forum?id=TiYOHdK35L>.
- 449 DeepSeek-AI. DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence, 2026.
- 450 Emily R. Doherty-Torstrick, Kate E. Walton, and Brian A. Fallon. Cyberchondria: Parsing Health  
451 Anxiety From Online Behavior. *Psychosomatics*, 57(4):390–400, 2016. ISSN 1545-7206. doi:  
452 10.1016/j.psym.2016.02.002.
- 453 Charles A. Dorison, et al. In COVID-19 Health Messaging, Loss Framing Increases Anxiety with  
454 Little-to-No Concomitant Benefits: Experimental Evidence from 84 Countries. *Affective Science*,  
455 3(3):577–602, September 2022. ISSN 2662-205X. doi: 10.1007/s42761-022-00128-3. URL  
456 <https://doi.org/10.1007/s42761-022-00128-3>.
- 457 Yang Du, Shuang Rong, Yangbo Sun, Buyun Liu, Yuxiao Wu, Linda G. Snetselaar, Robert B. Wal-  
458 lace, and Wei Bao. Association Between Frequency of Eating Away-From-Home Meals and Risk  
459 of All-Cause and Cause-Specific Mortality. *Journal of the Academy of Nutrition and Dietetics*,  
460 121(9):1741–1749.e1, September 2021. ISSN 2212-2672. doi: 10.1016/j.jand.2021.01.012.
- 461 L. Fernández de la Cruz, M. Rydell, B. Runeson, B. M. D’Onofrio, G. Brander, C. Rück, P. Lichten-  
462 stein, H. Larsson, and D. Mataix-Cols. Suicide in obsessive-compulsive disorder: a population-  
463 based study of 36788 Swedish patients. *Molecular Psychiatry*, 22(11):1626–1632, November  
464 2017. ISSN 1476-5578. doi: 10.1038/mp.2016.115.

 Rest of paper (reference and Appendix) is removed.