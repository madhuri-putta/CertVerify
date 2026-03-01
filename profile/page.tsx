"use client";
import Navbar from '@/components/Navbar';

export default function Profile() {
    return (
        <div className="min-h-screen bg-gray-900 text-white pt-20">
            <Navbar />
            <div className="max-w-screen-md mx-auto p-4">
                <div className="bg-gray-800 rounded-xl shadow-lg border border-gray-700 p-8">
                    <div className="flex flex-col items-center pb-10">
                        <div className="w-24 h-24 mb-3 rounded-full bg-gradient-to-r from-blue-500 to-purple-600 flex items-center justify-center text-3xl font-bold">
                            JD
                        </div>
                        <h5 className="mb-1 text-xl font-medium text-white">John Doe</h5>
                        <span className="text-sm text-gray-400">User</span>
                        <div className="flex mt-4 md:mt-6">
                            <button className="inline-flex items-center px-4 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                                Edit Profile
                            </button>
                        </div>
                    </div>

                    <div className="border-t border-gray-700 pt-6">
                        <h3 className="text-lg font-semibold mb-4 text-blue-400">My Uploads</h3>
                        <ul className="space-y-4">
                            <li className="flex items-center justify-between p-3 bg-gray-700 rounded-lg">
                                <span className="text-sm text-gray-300">Certificate_001.pdf</span>
                                <span className="text-xs text-green-400 bg-green-900/30 px-2 py-1 rounded">Verified Real</span>
                            </li>
                            <li className="flex items-center justify-between p-3 bg-gray-700 rounded-lg">
                                <span className="text-sm text-gray-300">Certificate_002.jpg</span>
                                <span className="text-xs text-red-400 bg-red-900/30 px-2 py-1 rounded">Detected Fake</span>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    );
}
