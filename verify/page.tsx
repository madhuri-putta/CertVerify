"use client";
import { useState } from 'react';
import Navbar from '@/components/Navbar';
import FileUpload from '@/components/FileUpload';

export default function VerifyCertificate() {
    const [result, setResult] = useState<any>(null);

    const handleUploadComplete = (data: any) => {
        setResult(data);
    };

    return (
        <div className="min-h-screen text-white pt-20">
            <Navbar />
            <div className="max-w-screen-xl mx-auto p-4">
                <h1 className="text-3xl font-bold mb-8 text-center text-blue-400">Verify Certificate</h1>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div className="bg-gray-800/60 backdrop-blur-md p-6 rounded-xl shadow-lg border border-gray-700">
                        <h2 className="text-xl font-semibold mb-4 text-gray-300">Upload to Verify</h2>
                        <FileUpload onUploadComplete={handleUploadComplete} />
                    </div>

                    <div className="bg-gray-800/60 backdrop-blur-md p-6 rounded-xl shadow-lg border border-gray-700">
                        <h2 className="text-xl font-semibold mb-4 text-gray-300">Verification Result</h2>
                        {result ? (
                            <div className="space-y-4">
                                <div className={`text-3xl font-bold ${result.is_real ? 'text-green-500' : 'text-red-500'}`}>
                                    {result.is_real ? 'GENUINE CERTIFICATE' : 'POTENTIAL FAKE'}
                                </div>

                                <div className="bg-gray-900/80 p-4 rounded-lg">
                                    <h3 className="font-bold text-gray-400 mb-2">Blockchain Status</h3>
                                    <p>{result.blockchain_verified ? '✅ Verified on Blockchain' : '❌ Not found on Blockchain'}</p>
                                </div>

                                <div className="bg-gray-900/80 p-4 rounded-lg">
                                    <h3 className="font-bold text-gray-400 mb-2">ML Analysis</h3>
                                    <p>Confidence: <span className="font-mono">{(result.ml_analysis.confidence * 100).toFixed(1)}%</span></p>
                                    <p>Reason: {result.ml_analysis.reason}</p>
                                </div>
                            </div>
                        ) : (
                            <div className="flex items-center justify-center h-64 border-2 border-dashed border-gray-700 rounded-lg">
                                <p className="text-gray-500">Waiting for upload...</p>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
