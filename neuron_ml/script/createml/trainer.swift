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
print("[Neuron - Swift] Arguments: \(args)")
let Dpath = args[1]
let train = "Train"
let test = "Test"
let out = args[2]
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
