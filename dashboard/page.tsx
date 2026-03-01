"use client";
import { useState, useEffect } from 'react';
import Navbar from '@/components/Navbar';
import FileUpload from '@/components/FileUpload';

export default function Dashboard() {
    const [result, setResult] = useState<any>(null);
    const [stats, setStats] = useState<any>(null);

    useEffect(() => {
        fetch('http://localhost:8000/api/admin/stats')
            .then(res => res.json())
            .then(data => setStats(data))
            .catch(err => console.error(err));
    }, []);

    const handleUploadComplete = (data: any) => {
        setResult(data);
    };

    return (
        <div className="min-h-screen text-white">
            <Navbar />

            {/* Hero Section with Upload Box */}
            <section className="pt-32 pb-16 px-4 mx-auto max-w-screen-xl text-center lg:pt-40 lg:px-12">
                <h1 className="mb-4 text-2xl font-extrabold tracking-tight leading-none text-white md:text-3xl lg:text-4xl">
                    Detect <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-600">Fake Certificates</span> with AI & Blockchain
                </h1>
                <p className="mb-8 text-lg font-normal text-gray-400 lg:text-xl sm:px-16 xl:px-48">
                    Secure, instant, and reliable verification for academic and professional credentials. Powered by advanced Machine Learning and immutable Blockchain technology.
                </p>

                {/* Upload Box Area */}
                <div className="max-w-3xl mx-auto mb-16">
                    <div className="bg-gray-800/60 backdrop-blur-md p-8 rounded-xl shadow-lg border border-gray-700">
                        <h2 className="text-xl font-semibold mb-6 text-blue-400 text-center">Verify Certificate Now</h2>
                        <FileUpload onUploadComplete={handleUploadComplete} />
                    </div>

                    {/* Results Section (Only visible after upload) */}
                    {result && (
                        <div className="mt-8 bg-gray-800/60 backdrop-blur-md p-8 rounded-xl shadow-lg border border-gray-700 animate-fade-in">
                            <h2 className="text-xl font-semibold mb-6 text-gray-300 text-center">Analysis Result</h2>
                            <div className="flex flex-col items-center justify-center">
                                <div className={`text-5xl font-bold mb-4 ${result.is_real ? 'text-green-500' : 'text-red-500'}`}>
                                    {result.is_real ? 'REAL' : 'FAKE'}
                                </div>
                                <div className="text-xl text-gray-300 mb-6">
                                    Confidence: {(result.ml_analysis.confidence * 100).toFixed(1)}%
                                </div>
                                <div className="w-full bg-gray-900/80 p-6 rounded-lg border border-gray-700 text-left">
                                    <p className="mb-2 text-lg"><span className="font-bold text-blue-400">Reason:</span> {result.ml_analysis.reason}</p>
                                    <p className="text-lg"><span className="font-bold text-purple-400">Blockchain Verified:</span> {result.blockchain_verified ? 'Yes' : 'No'}</p>
                                </div>
                            </div>
                        </div>
                    )}
                </div>
            </section>

            {/* Statistics Section */}
            {stats && (
                <section className="bg-gray-900/50 py-12 border-t border-gray-800">
                    <div className="max-w-screen-xl mx-auto px-4">
                        <h2 className="text-2xl font-bold mb-8 text-center text-gray-300">Live System Statistics</h2>
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
                            <div className="bg-gray-800/60 backdrop-blur-md p-6 rounded-lg border border-gray-700 text-center">
                                <h3 className="text-gray-400 mb-2">Total Issued</h3>
                                <p className="text-4xl font-bold text-white">{stats.total_issued}</p>
                            </div>
                            <div className="bg-gray-800/60 backdrop-blur-md p-6 rounded-lg border border-gray-700 text-center">
                                <h3 className="text-gray-400 mb-2">Total Verified</h3>
                                <p className="text-4xl font-bold text-green-400">{stats.total_verified}</p>
                            </div>
                            <div className="bg-gray-800/60 backdrop-blur-md p-6 rounded-lg border border-gray-700 text-center">
                                <h3 className="text-gray-400 mb-2">Fake Attempts</h3>
                                <p className="text-4xl font-bold text-red-400">{stats.fake_attempts}</p>
                            </div>
                        </div>

                        {/* Recent Activity Table */}
                        <h3 className="text-xl font-bold mb-6 text-gray-300 text-center">Recent Verifications</h3>
                        <div className="bg-gray-800/60 backdrop-blur-md rounded-lg overflow-hidden border border-gray-700">
                            <table className="w-full text-left text-gray-400">
                                <thead className="bg-gray-700/50 text-gray-200 uppercase text-sm">
                                    <tr>
                                        <th className="p-4">Student</th>
                                        <th className="p-4">Course</th>
                                        <th className="p-4">Institute</th>
                                        <th className="p-4">Status</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {stats.recent_activity.map((cert: any, index: number) => (
                                        <tr key={index} className="border-b border-gray-700 hover:bg-gray-700/50 transition">
                                            <td className="p-4 font-medium text-white">{cert.student_name}</td>
                                            <td className="p-4">{cert.course}</td>
                                            <td className="p-4">{cert.institute}</td>
                                            <td className={`p-4 font-bold ${cert.status === 'Valid' ? 'text-green-400' : 'text-red-400'}`}>{cert.status}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>
            )}

            {/* Features Section */}
            <section className="bg-gray-800/50 backdrop-blur-sm py-16">
                <div className="py-8 px-4 mx-auto max-w-screen-xl sm:py-16 lg:px-6">
                    <div className="space-y-8 md:grid md:grid-cols-2 lg:grid-cols-3 md:gap-12 md:space-y-0">
                        <div>
                            <div className="flex justify-center items-center mb-4 w-10 h-10 rounded-full bg-blue-900 lg:h-12 lg:w-12">
                                <svg className="w-5 h-5 text-blue-400 lg:w-6 lg:h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 00-1-1H3zm6 6a1 1 0 100-2 1 1 0 000 2z" clipRule="evenodd"></path></svg>
                            </div>
                            <h3 className="mb-2 text-xl font-bold dark:text-white">AI Analysis</h3>
                            <p className="text-gray-400">Our ML models analyze visual artifacts, font inconsistencies, and layout anomalies to detect forgeries.</p>
                        </div>
                        <div>
                            <div className="flex justify-center items-center mb-4 w-10 h-10 rounded-full bg-purple-900 lg:h-12 lg:w-12">
                                <svg className="w-5 h-5 text-purple-400 lg:w-6 lg:h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"></path><path fillRule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clipRule="evenodd"></path></svg>
                            </div>
                            <h3 className="mb-2 text-xl font-bold dark:text-white">Blockchain Verified</h3>
                            <p className="text-gray-400">Valid certificates are hashed and stored on the Ethereum blockchain for immutable proof of existence.</p>
                        </div>
                        <div>
                            <div className="flex justify-center items-center mb-4 w-10 h-10 rounded-full bg-green-900 lg:h-12 lg:w-12">
                                <svg className="w-5 h-5 text-green-400 lg:w-6 lg:h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clipRule="evenodd"></path></svg>
                            </div>
                            <h3 className="mb-2 text-xl font-bold dark:text-white">Instant Results</h3>
                            <p className="text-gray-400">Get verification results in seconds with a detailed breakdown of confidence scores and reasons.</p>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    );
}
