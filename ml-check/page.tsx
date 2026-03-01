"use client";
import { useState } from 'react';
import Navbar from '@/components/Navbar';
import FileUpload from '@/components/FileUpload';

export default function MLCheck() {
    const [result, setResult] = useState<any>(null);

    const handleUploadComplete = (data: any) => {
        setResult(data);
    };

    return (
        <div className="min-h-screen text-white pt-20">
            <Navbar />
            <div className="max-w-screen-xl mx-auto p-4">
                <h1 className="text-3xl font-bold mb-8 text-center text-purple-400">Advanced ML Detection</h1>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div className="bg-gray-800/60 backdrop-blur-md p-6 rounded-xl shadow-lg border border-gray-700">
                        <h2 className="text-xl font-semibold mb-4 text-gray-300">Upload for Deep Analysis</h2>
                        <FileUpload onUploadComplete={handleUploadComplete} />
                    </div>

                    <div className="bg-gray-800/60 backdrop-blur-md p-6 rounded-xl shadow-lg border border-gray-700">
                        <h2 className="text-xl font-semibold mb-4 text-gray-300">Detailed Analysis</h2>
                        {result ? (
                            <div className="space-y-6">

                                {/* Forgery Score */}
                                <div className="bg-gray-900/80 p-4 rounded-lg border border-gray-700">
                                    <h3 className="font-bold text-gray-400 mb-2">Tampering Score</h3>
                                    <div className="w-full bg-gray-700 rounded-full h-4 mb-2">
                                        <div
                                            className={`h-4 rounded-full ${result.ml_analysis.confidence > 0.5 ? 'bg-red-500' : 'bg-green-500'}`}
                                            style={{ width: `${result.ml_analysis.confidence * 100}%` }}
                                        ></div>
                                    </div>
                                    <p className="text-right text-sm">{(result.ml_analysis.confidence * 100).toFixed(1)}% Probability of Forgery</p>
                                </div>

                                {/* OCR Text */}
                                <div className="bg-gray-900/80 p-4 rounded-lg border border-gray-700">
                                    <h3 className="font-bold text-gray-400 mb-2">Extracted Text (OCR)</h3>
                                    <p className="font-mono text-sm text-gray-300 whitespace-pre-wrap">
                                        {/* Mock OCR data if not present in result yet */}
                                        {result.ocr_text || "Simulated Text Extraction:\nStudent: John Doe\nCourse: B.Tech CS\nYear: 2024"}
                                    </p>
                                </div>

                                {/* Flagged Areas */}
                                <div className="bg-gray-900/80 p-4 rounded-lg border border-gray-700">
                                    <h3 className="font-bold text-gray-400 mb-2">Flagged Anomalies</h3>
                                    <ul className="list-disc list-inside text-red-400">
                                        {result.ml_analysis.reason ? (
                                            <li>{result.ml_analysis.reason}</li>
                                        ) : (
                                            <li>No obvious anomalies detected.</li>
                                        )}
                                    </ul>
                                </div>

                            </div>
                        ) : (
                            <div className="flex items-center justify-center h-64 border-2 border-dashed border-gray-700 rounded-lg">
                                <p className="text-gray-500">Upload to see deepfake analysis...</p>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
