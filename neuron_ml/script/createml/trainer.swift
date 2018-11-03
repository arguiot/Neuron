#!/usr/bin/swift

/*
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

script/CreateML/trainer.swift will train and output the model

*/
// CreateML trainer
import CreateML
import Foundation

// Gets arguments
let args = CommandLine.arguments
let Dpath = args[0 + 2] // + 2 because `swift trainer.swift ...` already takes 2 useless arguments
let train = args[1 + 2]
let test = args[2 + 2]
let out = args[3 + 2]
// Specify where is the data
let path = NSString(string: Dpath).expandingTildeInPath
let trainingDir = URL(fileURLWithPath: path).appendingPathComponent(train)
let testDir = URL(fileURLWithPath: path).appendingPathComponent(test)

// Create a model
let model = try MLImageClassifier(trainingData: .labeledDirectories(at: trainingDir))

// Test the model
let evaluation = model.evaluation(on: .labeledDirectories(at: testDir))

// Save the model
try model.write(to: URL(fileURLWithPath: out))
