# Building Bixby Capsule

## 1. Create New Capsule

ID, version, format

tartget: bixby-device-lang-con

## 2. Creating Model

1. Creating model directory
2. Actions: function calls
3. Concept: objects used by function
4. One file per one action/ actions in one action dir
   1. input/ output (ex. Object)
   2. inputs can be multiple

5. Concept defines object in action file

   1. Defining types such as enum, text, name

   2. Structure type: returning several values that divided in fields // need to define concept per value

## 3. Training

1. Make lang dir in resource dir
2. Make training file
3. Need to set vocabulary for objects (esp. enum in vocab file)
4. Compiling
5. Debug

​		

## 4. Set Endpoint in JS

1. In code dir, make action.js file
2. Define function
3. In resources/lang/, make action.endpoints.bxb file
4. Require('http')
5. Build based on API



## 5. UI/UX

1. In resources dir, make UI kit file, action_layout.layout.bxb file
2. Use autocomplete of widgets and layout
3. Define detail view
4. Action_detail.layout.bxb
5. In content,, define each value i want to display
6. Each value has type such as image, paragraph
7. Each value has style which defines how to display

## 6. etc

1. Make capsule-info
2. Make hints
3. In hints, have some utterances to show users how to use your capsule